import discord
from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions
import requests

command_group = discord.SlashCommandGroup("emoji", "This is for copying emojis")

bot = None

@command_group.command(name="copy", description="Copy emojis from one server to another")
async def copy_emojis(ctx, emojis: str):
    server_id = ctx.guild_id
    server = bot.bot.get_guild(server_id)

    await ctx.respond("Attempting to copy emojis...")

    emojis = emojis.split(" ")
    all_emojis = []
    for emoji in emojis:

        emoji_name = emoji.split(":")[1]

        animated = False
        if emoji.split(":")[0] == "<a":
            animated = True

        id = int(emoji.split(":")[2].replace(">", ""))

        print(emoji)
        emoji = discord.PartialEmoji(name=emoji_name, animated=animated, id=id)

        image_url = emoji.url

        emoji = await server.create_custom_emoji(name=emoji.name, image=requests.get(image_url).content)
        all_emojis.append(emoji)

    emoji_str = ""
    for emoji in all_emojis:
        emoji_str += str(emoji) + " "

    await ctx.edit(content=f"Successfully copied {emoji_str} emojis to {server.name}!")


def setup(bot_instance):
    global bot
    bot = bot_instance
    bot.add_slash_command_group(command_group)
