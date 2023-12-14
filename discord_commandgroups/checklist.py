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
    response_str = "**List:**\n"
    for i in range(len(data)):
        list_item = data[i]
        if not list_item["completed"]:

            response_str += str(i+1) + ". \t " + list_item["name"]
            if list_item["description"] != "":
                response_str += ": " + list_item["description"]
            response_str += "\n"
    return response_str

@command_group.command(name="list_tasks", description="Gets the list of tasks to do")
async def list_tasks(ctx):
    await ctx.respond(get_response_str())

@command_group.command(name="create_task", description="Creates a task")
async def create_task(ctx, name: str, description: str=""):
    global data
    data.append({"completed": False, "name": name, "description": description})
    data = database.save("checklist", data)

    await ctx.respond("Added task " + name + " with description " + description)

@command_group.command(name="complete_task", description="Marks a task as complete")
async def complete_task(ctx, number: int):
    global data

    index = number - 1
    found = False
    for i in range(len(data)):
        if i == index:
            data[i]["complete"] = True
            found = True
            break

    if found:
        data = database.save("checklist", data)

        await ctx.respond(str(number) + " | " + data[index]["name"] + " marked as complete.")
    else:
        await ctx.respond("Cannot find task from index " + str(index))

@command_group.command(name="un_complete_task", description="Marks a task as incomplete")
async def un_complete_task(ctx, number: int):
    global data

    index = number - 1
    found = False
    for i in range(len(data)):
        if i == index:
            data[i]["complete"] = False
            found = True
            break

    if found:
        data = database.save("checklist", data)

        await ctx.respond(str(number) + " | " + data[index]["name"] + " marked as incomplete.")
    else:
        await ctx.respond("Cannot find task from index " + str(index))

def setup(bot_instance):
    global bot
    bot = bot_instance
    bot.add_slash_command_group(command_group)
