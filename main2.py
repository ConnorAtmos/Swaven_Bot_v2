import os, time
import subprocess as sp
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import scipy.io.wavfile as wavf

import discord

from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions
from toolbox import tts_local

from discord_commandgroups import verification_group
from discord_commandgroups import copy_emoji_group
from discord_commandgroups import moderation_group
from discord_commandgroups import tts_bot
from discord_commandgroups import chatgpt
from discord_commandgroups import checklist
from discord_commandgroups import discord_music_player

# sudo systemctl restart Tuley_Bot.service

current_directory = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    discord_key = database.load_key("tuley_bot")
    bot = discord_bot.discordBot(discord_key)
    bot.add_server_id(1182333772830617671)
    log_channel = 1184514187502821576

    vc_text_channel = 1184514346722795641

    #verification_group.setup(bot, log_channel) # This is removed as there is no need anymore due to onboarding.
    tts_bot.setup(bot, [vc_text_channel])
    copy_emoji_group.setup(bot)
    chatgpt.setup(bot)
    checklist.setup(bot, 1182342670866202714)
    moderation_group.setup(bot, log_channel)
    #discord_music_player.setup(bot)

    bot.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

