import discord
import cleantext
def get_role_names_from_string(ctx, role_str: str):
    """
    Params
    ------
    role_str: str
        A string of roles separated by commas (i.e. "role1, role2, role3")
        Also can be separated by spaces (i.e. "role1 role2 role3")
        This can be either the role name or the role id/mention

    Returns
    -------
    roles: list
        A list of role names

    Notes
    -----
    This function will remove duplicates as well

    Example:
    --------
    # This is an example of how to use this function, within a command
    role_str = "role1, role2, role3"
    roles = get_role_names_from_string(ctx, role_str)
    ctx.respond(f"Roles {roles} located.")
    """
    # Split roles be commas
    roles = role_str.split(",")
    # Split by " "  too
    roles = list(set(roles + role_str.split(" ")))
    # Remove spaces in all roles
    roles = [role.strip() for role in roles]

    # Get the name of all roles in roles list
    for i, role in enumerate(roles):
        # Strip the <@& and > from the role, if it exists
        if role.startswith("<@&") and role.endswith(">"):
            roles[i] = role[3:-1]
            role_number = int(roles[i])
            # Get the role name from the role id
            roles[i] = ctx.guild.get_role(role_number).name

    return roles


def get_role_id(ctx, role_name):
    """
    Params
    ------
    ctx: discord_slash.context.SlashContext
        The context of the command
    role_name: str
        The name of the role

    Returns
    -------
    role_id: int
        The id of the role

    Notes
    -----
    This function will raise an error if the role does not exist

    Example:
    --------
    # This is an example of how to use this function, within a command
    role_name = "role1"
    role_id = get_role_id(ctx, role_name)
    ctx.respond(f"Role {role_name} has id {role_id}")
    """
    # Get all roles in the server
    server_roles = ctx.guild.roles
    # Get all role names in the server
    server_role_names = [role.name for role in server_roles]

    # Get the role id, not the role name
    role_id = server_roles[server_role_names.index(role_name)].id

    return role_id

def remove_emoji_numbers(text: str):
    """
    Params
    ------
    text: str
        The text to remove numbers from

    Returns
    -------
    text: str
        The text with numbers removed

    Notes
    -----
    This function removes numbers from discord emojis for tts. (i.e. <:emoji:123456789> to emoji)

    Example:
    --------
    text = remove_emoji_numbers(text)
    """
    # Remove nubmers from the text if it is in an emoji format (i.e. <:emoji:123456789> to emoji)
    print(text)
    while text.find("<:") != -1:
        start = text.find("<:")
        middle = text.find(":", start + 2)
        end = text.find(">", middle + 1)

        text = text[:start] + text[start + 2:middle] + text[end + 1:]
    while text.find("<a:") != -1:
        start = text.find("<a:")
        middle = text.find(":", start + 3)
        end = text.find(">", middle + 1)

        text = text[:start] + text[start + 3:middle] + text[end + 1:]

    text = cleantext.replace_urls(text, "a link")
    text = cleantext.replace_phone_numbers(text, "a phone number")
    text = cleantext.replace_numbers(text, "a number")
    text = cleantext.replace_emails(text, "an email")
    return text


def convert_ping_to_username(text, guild):
    # Remove @ from the text if it is in a ping format (i.e. <@123456789> to 123456789 then to username)
    while text.find("<@") != -1:
        start = text.find("<@")
        end = text.find(">", start+2)

        user_id = int(text[start+2:end])
        user = guild.get_member(user_id)
        text = text[:start] +user.name + text[end+1:]
    return text


def get_emoji_from_id(ctx, id) -> str:
    """
    Params
    ------
    ctx: discord_slash.context.SlashContext
        The context of the command
    id: int
        The id of the emoji

    Returns
    -------
    emoji: str
        The emoji
    """
    # Get the emoji from the id
    for emoji in ctx.guild.emojis:
        if emoji.id == id:
            return str(emoji)
