import discord
from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions

command_group = discord.SlashCommandGroup("verification", "This is for the verification system")
command_group_mod = discord.SlashCommandGroup("verification_mod", "This is to manage verifying people")

bot = None

@command_group_mod.command(name="add_verification_role", description="This is a command that adds roles when users are verified")
async def add_verification_role(ctx, role: str):
    roles = discord_functions.get_role_names_from_string(ctx, role)
    # Get all roles in the server
    server_roles = ctx.guild.roles
    # Get all role names in the server
    server_role_names = [role.name for role in server_roles]
    # Check if all roles are in the server
    for role in roles:
        if role not in server_role_names:
            await ctx.respond(f"Role {role} does not exist in the server")
            return
    # Add roles to database
    database_name = str(ctx.guild.id) + "_verification_roles"
    # Get all roles in the database
    try:
        database_roles = database.get(database_name)
    except:
        database_roles = []
    # Append new roles to database
    roles += database_roles
    # Remove duplicates
    roles = list(set(roles))
    # Save to database
    database.save(database_name, roles)
    ping_str = ""
    # We want to get the role id, not the role name
    for role in roles:
        role_id = discord_functions.get_role_id(ctx, role)
        ping_str += f"<@&{role_id}> "
    await ctx.respond(f"Roles {ping_str} have been added to the verification roles")


@command_group_mod.command(name="get_verfication_roles", description="This is a command that gets all the roles that are added when a user is verified")
async def get_verification_roles(ctx):
    database_name = str(ctx.guild.id) + "_verification_roles"
    roles = database.get(database_name)
    ping_str = ""
    # We want to get the role id, not the role name
    for role in roles:
        role_id = discord_functions.get_role_id(ctx, role)
        ping_str += f"<@&{role_id}> "
    if len(roles) == 0:
        await ctx.respond(f"There are no roles for verification")
    else:
        await ctx.respond(f"The current verification roles are {ping_str}")


@command_group_mod.command(name="remove_verification_role", description="This is a command that removes roles when users are verified")
async def remove_verification_role(ctx, role: str):
    roles = discord_functions.get_role_names_from_string(ctx, role)
    # Get all roles in the server
    server_roles = ctx.guild.roles
    # Get all role names in the server
    server_role_names = [role.name for role in server_roles]
    # Check if all roles are in the server
    for role in roles:
        if role not in server_role_names:
            await ctx.respond(f"Role {role} does not exist in the server")
            return
    # Add roles to database
    database_name = str(ctx.guild.id) + "_verification_roles"
    # Get all roles in the database
    try:
        database_roles = database.get(database_name)
    except:
        database_roles = []
    # Check if all roles are in the database
    for role in roles:
        if role not in database_roles:
            role_id = discord_functions.get_role_id(ctx, role)
            role = f"<@&{role_id}>"
            await ctx.respond(f"Role {role} does not exist in the database")
            return
    # Remove roles from database
    for role in roles:
        if role in database_roles:
            database_roles.remove(role)
    # Save to database
    database.save(database_name, database_roles)
    ping_str = ""
    # We want to get the role id, not the role name
    for role in roles:
        role_id = discord_functions.get_role_id(ctx, role)
        ping_str += f"<@&{role_id}> "
    await ctx.respond(f"Roles {ping_str} have been removed from the verification roles")


@command_group.command(name="verify", description="This is a command that verifies you")
async def verify(ctx):
    # Get all roles in the database
    database_name = str(ctx.guild.id) + "_verification_roles"
    try:
        roles = database.get(database_name)
    except:
        roles = []
    # Get all roles in the server
    server_roles = ctx.guild.roles
    # Get all role names in the server
    server_role_names = [role.name for role in server_roles]
    # Check if all roles are in the server
    for role in roles:
        if role not in server_role_names:
            await ctx.respond(f"Role {role} does not exist in the server")
            return
    # Give user roles
    for role in roles:
        role_id = discord_functions.get_role_id(ctx, role)
        # Get role object
        role_id = discord.utils.get(ctx.guild.roles, id=role_id)
        await ctx.author.add_roles(role_id)
    await ctx.respond(f"You have been verified!")


def setup(bot_instance):
    global bot
    bot = bot_instance
    bot.add_slash_command_group(command_group)
    bot.add_slash_command_group(command_group_mod)
