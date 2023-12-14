import discord
from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions
import requests

command_group = discord.SlashCommandGroup("checklist", "This is for checklist")

try:
    data = database.get("checklist")
except:
    data = database.save("checklist", [])

bot = None

def get_response_str():
    global data
    response_str = "**List:**"
    for i in range(len(data)):
        list_item = data[i]
        if list_item["completed"]:
            response_str += str(i) + " | " + list_item["completed"] + " - " + list_item["name"] + ": " + list_item["description"] + "\n"
    return response_str

@command_group.command(name="get_list", description="Gets the list of items to do")
async def get_list(ctx):
    await ctx.respond(get_response_str())

@command_group.command(name="create_task", description="Creates a task")
async def create_task(ctx, name: str, description: str=""):
    global data
    data.append({"completed": False, "name": name, "description": description})
    database.save("checklist", data)

    await ctx.respond("Added task " + name + " with description " + description)

@command_group.command(name="complete_task", description="Marks a task as complete")
async def complete_task(ctx, index: int):
    global data

    found = False
    for i in range(len(data)):
        if i == index:
            data[i]["complete"] = True
            found = True
            break

    if found:
        database.save("checklist", data)

        await ctx.respond(data[index]["name"] + " marked as complete.")
    else:
        await ctx.respond("Cannot find task from index " + str(index))

def setup(bot_instance):
    global bot
    bot = bot_instance
    bot.add_slash_command_group(command_group)
