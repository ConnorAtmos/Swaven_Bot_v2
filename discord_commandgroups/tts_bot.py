import discord, random, os
from toolbox import database
from toolbox import discord_bot
from toolbox import discord_functions
from discord import commands
import requests, asyncio, multiprocessing
from toolbox import tts_local
import time
bot = None
vc_text_channel = None

database.set_storage_path("storage")

models = ["tts_models/en/ljspeech/tacotron2-DCA", "tts_models/multilingual/multi-dataset/xtts_v2", "tts_models/en/ljspeech/tacotron2-DDC","tts_models/en/ljspeech/overflow", "tts_models/en/vctk/vits"]
tts_local.set_tts(models[-1])

command_group = discord.SlashCommandGroup("vc_tts", "This is for tts commands")


quirky_response = ""

def setup(bot_instance, vc_text__channel_id, end_text = ""):
    global quirky_response
    global bot
    global vc_text_channel
    if end_text:
        quirky_response = end_text

    bot = bot_instance
    vc_text_channel = vc_text__channel_id

    current_author = {}


    @bot.bot.event
    async def on_message(message):
        if message.channel.id == vc_text_channel:
            text_content = message.content

            # Remove emoji numbers and only say the text
            text_content = discord_functions.remove_emoji_numbers(text_content)

            # Convert user mentions to names
            text_content = discord_functions.convert_ping_to_username(text_content, guild=message.guild)

            # Clean up remaining text
            text_content = discord_functions.clean_up_rest_of_text(text_content)

            # See if the user is in a voice channel
            if message.author.voice is not None and not message.author.bot:

                author_id = message.author.id
                voice_channel = message.author.voice.channel
                author_name = message.author.name

                if voice_channel.guild.voice_client is not None and voice_channel.guild.voice_client.channel.id != voice_channel.id:
                    await voice_channel.guild.voice_client.disconnect()

                # If the bot is already in the voice channel of the user, use that
                if voice_channel.guild.voice_client is not None:
                    vc = voice_channel.guild.voice_client
                else:
                    vc = await voice_channel.connect()

                vc_id = vc.channel.id

                diff_author = False
                if vc_id not in current_author:
                    current_author[vc_id] = [author_id, time.time()]
                    diff_author = True
                elif current_author[vc_id][0] != author_id or abs(time.time() - current_author[vc_id][1]) > 5:
                    diff_author = True

                if diff_author:
                    text = f"{author_name} said {text_content}{quirky_response}"
                else:
                    text = f"{text_content}{quirky_response}"
                # wav_content is in bytes, not a file

                #await message.channel.send(owoify.owoify(text_content, "uwu"))

                await tts_local.tts_wav(bot.bot, text, f"storage/{author_id}.wav")


                data = discord.FFmpegOpusAudio(f"storage/{author_id}.wav")
                current_author[vc_id] = [author_id, time.time()]

                # Play the wav content
                if vc.is_playing():
                    vc.stop()
                    await asyncio.sleep(0.3)
                vc.play(data)

    @bot.bot.event
    async def on_voice_state_update(member, before, after):
        if not member.id == bot.bot.user.id:
            return

        elif before.channel is None:
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 600:  # 600:
                    file_dir = os.path.dirname(os.path.realpath(__file__))
                    with open(os.path.join(file_dir, "pickup_lines.txt"), "r+", encoding="utf-8") as f:
                        # UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 88: ordinal not in range(128)
                        lines = f.readlines()
                        random_line = random.choice(lines).strip()

                    await tts_local.tts_wav(bot.bot, random_line + ". Now I gotta go, bye.", f"storage/leave_audio.wav")

                    data = discord.FFmpegOpusAudio(f"storage/leave_audio.wav")
                    voice.play(data)
                    while voice.is_playing():
                        await asyncio.sleep(0.2)

                    await voice.disconnect()
                if not voice.is_connected():
                    break
