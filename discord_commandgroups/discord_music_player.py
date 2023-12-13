import wavelink, asyncio
import discord

bot = None

command_group = discord.SlashCommandGroup("music", "This is for music player")

async def connect_nodes():
    global bot
    """Connect to our Lavalink nodes."""
    await bot.bot.wait_until_ready()  # wait until the bot is ready

    await wavelink.NodePool.create_node(
        bot=bot.bot,
        host='127.0.0.1',
        port=2333,
        password='youshallnotpass'
    )  # create a node


play_queue = []
queue_running = False


async def play_song(song, ctx):
    global play_queue
    vc = ctx.voice_client  # define our voice client

    if not vc:  # check if the bot is not in a voice channel
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # connect to the voice channel

    if ctx.author.voice.channel.id != vc.channel.id:  # check if the bot is not in the voice channel
        return await ctx.respond("You must be in the same voice channel as the bot.")  # return an error message

    await vc.play(song)  # play the song

    await ctx.respond(f"Now playing: `{vc.source.title}`: {vc.source.uri}")  # return a message

    if len(play_queue) > 1:
        await ctx.respond(f"Next up is `{play_queue[1].title}` (Songs in queue: {len(play_queue)})")


stop_queue = False


async def run_queue(ctx, top=True):
    global play_queue
    global stop_queue

    # We wait until the song is done playing, just in case the bot is lagging behind.
    while ctx.voice_client is not None and ctx.voice_client.is_playing():
        await asyncio.sleep(1)

    if len(play_queue) > 0:
        if not stop_queue:
            await play_song(play_queue[0], ctx)
            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)
        play_queue.pop(0)
        await run_queue(ctx, top=False)
    if top:
        await ctx.respond("Finished playing queue.")
        stop_queue = False


@command_group.command(name="skip")
async def skip(ctx):
    global queue_running
    vc = ctx.voice_client  # define our voice client

    if not vc:  # check if the bot is not in a voice channel
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # connect to the voice channel

    if ctx.author.voice.channel.id != vc.channel.id:  # check if the bot is not in the voice channel
        return await ctx.respond("You must be in the same voice channel as the bot.")  # return an error message

    await vc.stop()
    await ctx.respond("Skipped the song.")
    if not queue_running:
        queue_running = True
        await run_queue(ctx)
        queue_running = False


@command_group.command(name="stop")
async def stop(ctx):
    global stop_queue
    stop_queue = True
    await skip(ctx)
    await ctx.respond("Stopped playing.")

@command_group.command(name="queue")
async def queue(ctx):
    global play_queue
    response_text = ""
    for i in range(len(play_queue)):
        response_text += f"{i+1}: {play_queue[i].title}\n"
        if i == 10:
            response_text += f"and {len(play_queue) - 10} more..."
            break
    await ctx.respond(f"Current queue: ```{response_text}```")




@command_group.command(name="play")
async def play(ctx, search: str):
    global play_queue
    global queue_running

    song = await wavelink.YouTubeTrack.search(query=search, return_first=True)  # search for the song

    if not song:  # check if the song is not found
        return await ctx.respond("No song found.")  # return an error message

    play_queue.append(song)
    queue_position = len(play_queue)
    await ctx.respond(f"Added `{song.title}` to the queue. Current position is {queue_position}: {song.uri}")

    if not queue_running:
        queue_running = True
        await run_queue(ctx)
        queue_running = False


def setup(bot_instance):
    global bot
    bot = bot_instance
    bot.add_slash_command_group(command_group)

    @bot.bot.event
    async def on_ready():
        print("Connecting nodes")
        await connect_nodes()  # connect to the server
        print("Nodes connected")

    @bot.bot.event
    async def on_wavelink_node_ready(node: wavelink.Node):
        print(f"{node.identifier} is ready.")  # print a message

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
                if time == 600:

                    await voice.disconnect()
                if not voice.is_connected():
                    break