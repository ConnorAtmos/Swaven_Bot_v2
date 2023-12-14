import discord
from openai import OpenAI
from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions
import owoify
import requests

client = OpenAI(api_key = database.load_key("chatgpt"))

command_group = discord.SlashCommandGroup("chatgpt", "Chatting and responses")

bot = None

messages = {}

role = {"role": "system", "content": "You are discord bot. Maximum character limit of your response is 2000. Any code must be surrounded by ``` and ```. If java, do ```java //code ```"}

async def run_gpt(ctx, user_id, version, message, owo_text=False):
    if user_id not in messages.keys():
        messages[user_id] = []

    usr_messages = messages[user_id]

    usr_messages.append({"role": "user", "content": message})

    await ctx.respond("**You:** \n" + message)

    print(usr_messages)

    information = [role]
    for msg in usr_messages:
        information.append(msg)

    completion = client.chat.completions.create(
        model=version,
        messages=information
    )

    response = completion.choices[0].message.content

    usr_messages.append({"role": "assistant", "content": response})

    while len(usr_messages) > 15:
        usr_messages.pop(0)

    if owo_text:
        response = owoify.owoify(response, "owo")

    await ctx.respond("**GPT:** \n" + response)
@command_group.command(name="gpt3", description="Send a message to chatgpt 3 for a response")
async def gpt3(ctx, message: str):
    user_id = ctx.user.id
    await run_gpt(ctx, user_id, "gpt-3.5-turbo", message)

@command_group.command(name="owopt", description="Send a message to chatgpt owo for a response")
async def owopt(ctx, message: str):
    user_id = ctx.user.id
    await run_gpt(ctx, user_id, "gpt-3.5-turbo", message, owo_text=True)

@command_group.command(name="gpt4", description="Send a message to chatgpt 4 for a response")
async def gpt4(ctx, message: str):
    user_id = ctx.user.id
    await run_gpt(ctx, user_id, "gpt-3.5-turbo", message)


def setup(bot_instance):
    global bot
    bot = bot_instance
    bot.add_slash_command_group(command_group)
