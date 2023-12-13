import discord
from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions

command_group = discord.SlashCommandGroup("moderation", "This is for moderation commands")

bot = None
log_channel = 12345


@command_group.command(name="delete", description="Deletes a group of messages")
async def delete(ctx, amount: int):
    await ctx.respond(f"Deleting {amount} messages")
    await ctx.channel.purge(limit=amount)
    await ctx.edit(content=f"Deleted messages in {ctx.channel.name}")


@command_group.command(name="delete_for_user", description="Deletes a group of messages from a user")
async def delete_for_user(ctx, amount: int, user: discord.Member):
    await ctx.respond(f"Deleting {amount} messages from {user.name}")
    await ctx.channel.purge(limit=amount, check=lambda m: m.author == user)
    await ctx.edit(content=f"Deleted {amount} messages from {user.name}")


@command_group.command(name="kick", description="Kicks a user, and deletes their messages")
async def ban(ctx, user: discord.Member, reason: str):
    await ctx.respond(f"Banning {user.name} for {reason}")
    await user.kick(reason=reason)
    await ctx.edit(content=f"Banned {user.name} for {reason}")


def setup(bot_instance, message_log_id):
    global bot
    global log_channel
    bot = bot_instance
    log_channel = message_log_id
    bot.add_slash_command_group(command_group)