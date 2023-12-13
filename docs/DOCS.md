[Back to README.md](/README.md)

# DOCUMENTATION TABLE OF CONTENTS #

This is the documentation for the project Swaven_Bot.

## INSTRUCTIONS.md ##

[0. HOW TO USE THIS TEMPLATE](/docs/INSTRUCTIONS.md#0-how-to-use-this-template)

[1. HOW TO INSTALL ANACONDA](/docs/INSTRUCTIONS.md#1-how-to-install-anaconda)

[2. HOW TO CREATE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#2-how-to-create-conda-environment)

[3. HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY](/docs/INSTRUCTIONS.md#3-how-to-connect-interpreter-to-jetbrains-gateway)

[4. HOW TO INSTALL REQUIREMENTS](/docs/INSTRUCTIONS.md#4-how-to-install-requirements)

[5. HOW TO INSTALL SERVICE](/docs/INSTRUCTIONS.md#5-how-to-install-service)

[6. HOW TO INSTALL LAVALINK](/docs/INSTRUCTIONS.md#6-how-to-install-lavalink)

[A. HOW TO REMOVE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#a-how-to-remove-conda-environment)

[B. HOW TO UNINSTALL SERVICE](/docs/INSTRUCTIONS.md#b-how-to-uninstall-service)

# API #


<details>
<summary>

## Documentation For [discord_commandgroups/verification_group.py](/docs/DISCORD_COMMANDGROUPS-VERIFICATION_GROUP.md)

</summary>


 <details>
<summary>

### > [function setup](/docs/DISCORD_COMMANDGROUPS-VERIFICATION_GROUP.md#function-setup) 



</summary>

[def setup(bot_instance):](./../discord_commandgroups/verification_group.py#L125) 



</details>

<br></details>


<details>
<summary>

## Documentation For [discord_commandgroups/discord_music_player.py](/docs/DISCORD_COMMANDGROUPS-DISCORD_MUSIC_PLAYER.md)

</summary>


 <details>
<summary>

### > [function setup](/docs/DISCORD_COMMANDGROUPS-DISCORD_MUSIC_PLAYER.md#function-setup) 



</summary>

[def setup(bot_instance):](./../discord_commandgroups/discord_music_player.py#L126) 



</details>

<br></details>


<details>
<summary>

## Documentation For [discord_commandgroups/copy_emoji_group.py](/docs/DISCORD_COMMANDGROUPS-COPY_EMOJI_GROUP.md)

</summary>


 <details>
<summary>

### > [function setup](/docs/DISCORD_COMMANDGROUPS-COPY_EMOJI_GROUP.md#function-setup) 



</summary>

[def setup(bot_instance):](./../discord_commandgroups/copy_emoji_group.py#L45) 



</details>

<br></details>


<details>
<summary>

## Documentation For [discord_commandgroups/moderation_group.py](/docs/DISCORD_COMMANDGROUPS-MODERATION_GROUP.md)

</summary>


 <details>
<summary>

### > [function setup](/docs/DISCORD_COMMANDGROUPS-MODERATION_GROUP.md#function-setup) 



</summary>

[def setup(bot_instance, message_log_id):](./../discord_commandgroups/moderation_group.py#L33) 



</details>

<br></details>


<details>
<summary>

## Documentation For [discord_commandgroups/tts_bot.py](/docs/DISCORD_COMMANDGROUPS-TTS_BOT.md)

</summary>


 <details>
<summary>

### > [function set_male_role](/docs/DISCORD_COMMANDGROUPS-TTS_BOT.md#function-set_male_role) 



</summary>

[def set_male_role(role_id:int):](./../discord_commandgroups/tts_bot.py#L21) 



</details>


 <details>
<summary>

### > [function setup](/docs/DISCORD_COMMANDGROUPS-TTS_BOT.md#function-setup) 



</summary>

[def setup(bot_instance, vc_text__channel_id):](./../discord_commandgroups/tts_bot.py#L26) 



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/tts_local.py](/docs/TOOLBOX-TTS_LOCAL.md)

</summary>


 <details>
<summary>

### > [function set_tts](/docs/TOOLBOX-TTS_LOCAL.md#function-set_tts) 



</summary>

[def set_tts(model:str):](./../toolbox/tts_local.py#L12) 

Param


```python
    text: str
        Text to be converted to speech
```

Return


```python
    None
```



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/discord_functions.py](/docs/TOOLBOX-DISCORD_FUNCTIONS.md)

</summary>


 <details>
<summary>

### > [function get_role_names_from_string](/docs/TOOLBOX-DISCORD_FUNCTIONS.md#function-get_role_names_from_string) 



</summary>

[def get_role_names_from_string(ctx, role_str: str):](./../toolbox/discord_functions.py#L3) 

Note


```python
    This function will remove duplicates as well
```

Param


```python
    role_str: str
        A string of roles separated by commas (i.e. "role1, role2, role3")
        Also can be separated by spaces (i.e. "role1 role2 role3")
        This can be either the role name or the role id/mention
```

Return


```python
    roles: list
        A list of role names
```

Example


```python
    # This is an example of how to use this function, within a command
    role_str = "role1, role2, role3"
    roles = get_role_names_from_string(ctx, role_str)
    ctx.respond(f"Roles {roles} located.")
```



</details>


 <details>
<summary>

### > [function get_role_id](/docs/TOOLBOX-DISCORD_FUNCTIONS.md#function-get_role_id) 



</summary>

[def get_role_id(ctx, role_name):](./../toolbox/discord_functions.py#L47) 

Note


```python
    This function will raise an error if the role does not exist
```

Param


```python
    ctx: discord_slash.context.SlashContext
        The context of the command
    role_name: str
        The name of the role
```

Return


```python
    role_id: int
        The id of the role
```

Example


```python
    # This is an example of how to use this function, within a command
    role_name = "role1"
    role_id = get_role_id(ctx, role_name)
    ctx.respond(f"Role {role_name} has id {role_id}")
```



</details>


 <details>
<summary>

### > [function remove_emoji_numbers](/docs/TOOLBOX-DISCORD_FUNCTIONS.md#function-remove_emoji_numbers) 



</summary>

[def remove_emoji_numbers(text: str):](./../toolbox/discord_functions.py#L82) 

Note


```python
    This function removes numbers from discord emojis for tts. (i.e. <:emoji:123456789> to emoji)
```

Param


```python
    text: str
        The text to remove numbers from
```

Return


```python
    text: str
        The text with numbers removed
```

Example


```python
    text = remove_emoji_numbers(text)
```



</details>


 <details>
<summary>

### > [function convert_ping_to_username](/docs/TOOLBOX-DISCORD_FUNCTIONS.md#function-convert_ping_to_username) 



</summary>

[def convert_ping_to_username(text, guild):](./../toolbox/discord_functions.py#L113) 



</details>


 <details>
<summary>

### > [function get_emoji_from_id](/docs/TOOLBOX-DISCORD_FUNCTIONS.md#function-get_emoji_from_id) 



</summary>

[def get_emoji_from_id(ctx, id) -> str:](./../toolbox/discord_functions.py#L125) 

Param


```python
    ctx: discord_slash.context.SlashContext
        The context of the command
    id: int
        The id of the emoji
```

Return


```python
    emoji: str
        The emoji
```



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/database.py](/docs/TOOLBOX-DATABASE.md)

</summary>


 <details>
<summary>

### > [function set_storage_path](/docs/TOOLBOX-DATABASE.md#function-set_storage_path) 



</summary>

[def set_storage_path(path):](./../toolbox/database.py#L8) 

Note


```python
    This function is used to set the path to the folder where the database files will be stored
```

Param


```python
ters
    ----------
    path : str
        The path to the folder where the database files will be stored
```

Return


```python
    None
        This function does not return anything
```

Example


```python
    set_storage_path('C:/Users/JohnDoe/Documents/MyDatabase')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function slugify](/docs/TOOLBOX-DATABASE.md#function-slugify) 



</summary>

[def slugify(value, allow_unicode=False):](./../toolbox/database.py#L40) 

Note


```python
    This function is used to slugify strings, which basically means to remove all special characters and replace them with dashes.
    This is useful for creating file names from strings.
```

Param


```python
ters
    ----------
    value : str
        The string to be slugified
    allow_unicode : bool
        Whether or not to allow unicode characters
```

Return


```python
    str
        The slugified string
```

Example


```python
    a = slugify('Hello World')
```

Reference


```python
    https://github.com/django/django/blob/master/django/utils/text.py
```



</details>


 <details>
<summary>

### > [function get](/docs/TOOLBOX-DATABASE.md#function-get) 



</summary>

[def get(name: str) -> object:](./../toolbox/database.py#L76) 

Note


```python
    This function is used to load objects from the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be loaded
```

Return


```python
    object or None
        The object loaded from the file, could be anything
```

Example


```python
    spreadsheet_data = get('spreadsheet_people')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function save](/docs/TOOLBOX-DATABASE.md#function-save) 



</summary>

[def save(name: str, data: any) -> None:](./../toolbox/database.py#L107) 

Note


```python
    This function is used to save objects to the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be saved
    data : any
        The data to be saved
```

Return


```python
    None
        This function does not return anything
```

Example


```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function delete_database](/docs/TOOLBOX-DATABASE.md#function-delete_database) 



</summary>

[def delete_database(name: str) -> object:](./../toolbox/database.py#L142) 

Note


```python
    This function is used to delete objects from the database folder
```

Param


```python
ters
    ----------
    name : str
        The name of the file to be deleted
```

Return


```python
    object or None
        The object loaded from the file, could be anything
```

Example


```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)

    delete_database('spreadsheet_people')
```

Reference


```python
    No Links
```



</details>


 <details>
<summary>

### > [function save_key](/docs/TOOLBOX-DATABASE.md#function-save_key) 



</summary>

[def save_key(platform: str, key: str, override: bool = False) -> None:](./../toolbox/database.py#L180) 

Note


```python
    This function is used to save keys in a secure location
```

Param


```python
ters
    ----------
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. '<google_api_key>')
    override: bool
        Whether or not to override the key if it already exists
```

Return


```python
    None
        This function does not return anything
```

Example


```python
    save_key('google', '<google_api_key>')
```

Reference


```python
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```



</details>


 <details>
<summary>

### > [function load_key](/docs/TOOLBOX-DATABASE.md#function-load_key) 



</summary>

[def load_key(platform: str) -> str:](./../toolbox/database.py#L227) 

Note


```python
        This function is used to load keys from a secure location
```

Param


```python
ters
        ----------
        platform: str
            The key to be loaded (e.g. '<google_api_key>')
```

Return


```python
        str or None
            This function returns the key if it exists, otherwise it returns None
```

Example


```python
        key = load_key('google')
```

Reference


```python
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/discord_bot.py](/docs/TOOLBOX-DISCORD_BOT.md)

</summary>


 <details>
<summary>

### > [class discordBot](/docs/TOOLBOX-DISCORD_BOT.md#class-discordbot) 



</summary>

[class discordBot:](./../toolbox/discord_bot.py#L4) 

Note


```python
        This class is used to create a Discord Bot.
```

Param


```python
ters
        ----------
        api_token : str
            The API token of the Discord Bot
```

Return


```python
        None
```

Example


```python
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.run()
```

Reference


```python
        https://docs.pycord.dev/en/stable/
```




 <details>
<summary>

### >  > [function discordBot.init](/docs/TOOLBOX-DISCORD_BOT.md#function-discordbotinit) 



</summary>

[def __init__(self, api_token: str) -> None:](./../toolbox/discord_bot.py#L5) 

Note


```python
        This class is used to create a Discord Bot.
```

Param


```python
ters
        ----------
        api_token : str
            The API token of the Discord Bot
```

Return


```python
        None
```

Example


```python
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.run()
```

Reference


```python
        https://docs.pycord.dev/en/stable/
```



</details>


 <details>
<summary>

### >  > [function discordBot.add_server_id](/docs/TOOLBOX-DISCORD_BOT.md#function-discordbotadd_server_id) 



</summary>

[def add_server_id(self, server_id: int) -> None:](./../toolbox/discord_bot.py#L36) 

Note


```python
        This function is used to add a server ID to the bot.
```

Param


```python
ters
        ----------
        server_id : int
            The ID of the server to add the bot to
```

Return


```python
        None
```

Example


```python
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.add_server_id(123456789)

        @bot.bot.slash_command(name="hello", guild_ids=bot.guild_ids)
        async def hello(ctx, name: str = "World"):
            await ctx.send(f"Hello {name}!")

        bot.run()
```

Reference


```python
        https://docs.pycord.dev/en/stable/
```



</details>


 <details>
<summary>

### >  > [function discordBot.add_server_ids](/docs/TOOLBOX-DISCORD_BOT.md#function-discordbotadd_server_ids) 



</summary>

[def add_server_ids(self, server_ids: list) -> None:](./../toolbox/discord_bot.py#L70) 

Note


```python
        This function is used to add a list of server IDs to the bot.
```

Param


```python
ters
        ----------
        server_ids : list
            The IDs of the servers to add the bot to
```

Return


```python
        None
```

Example


```python
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        server_ids = [123456789, 987654321]
        bot.add_server_ids(server_ids)

        @bot.bot.slash_command(name="hello", guild_ids=bot.guild_ids)
        async def hello(ctx, name: str = "World"):
            await ctx.send(f"Hello {name}!")


        bot.run()
```

Reference


```python
        https://docs.pycord.dev/en/stable/
```



</details>


 <details>
<summary>

### >  > [function discordBot.add_slash_command_group](/docs/TOOLBOX-DISCORD_BOT.md#function-discordbotadd_slash_command_group) 



</summary>

[def add_slash_command_group(self, slash_command_group) -> None:](./../toolbox/discord_bot.py#L106) 

Note


```python
        This function is used to add a list of server IDs to the bot.
```

Param


```python
ters
        ----------
        slash_command_group
            The IDs of the servers to add the bot to.
```

Return


```python
        None
```

Example


```python
        from discord_bot import discordBot
        import discord
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)

        server_ids = [123456789, 987654321]
        bot.add_server_ids(server_ids)

        command_group = discord.SlashCommandGroup(name="test", description="test")

        @command_group.command(name="hello", description="hello", guild_ids=bot.guild_ids)
        async def hello(ctx, name: str = "World"):
            await ctx.send(f"Hello {name}!")

        @command_group.command(name="goodbye", description="goodbye", guild_ids=bot.guild_ids)
        async def goodbye(ctx, name: str = "World"):
            await ctx.send(f"Goodbye {name}!")

        bot.add_slash_command_group(command_group)

        bot.run()
```

Reference


```python
        https://docs.pycord.dev/en/stable/
```



</details>


 <details>
<summary>

### >  > [function discordBot.run](/docs/TOOLBOX-DISCORD_BOT.md#function-discordbotrun) 



</summary>

[def run(self) -> None:](./../toolbox/discord_bot.py#L151) 

Note


```python
        This function is used to run the Discord Bot.
```

Param


```python
ters
        ----------
        None
```

Return


```python
        None
```

Example


```python
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.run()
```

Reference


```python
        https://docs.pycord.dev/en/stable/
```



</details>

</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/queue_local.py](/docs/TOOLBOX-QUEUE_LOCAL.md)

</summary>


 <details>
<summary>

### > [class Queue](/docs/TOOLBOX-QUEUE_LOCAL.md#class-queue) 



</summary>

[class Queue:](./../toolbox/queue_local.py#L2) 

Note


```python
    A queue is a data structure that follows the First In First Out (FIFO) principle.
    This means that the first item added to the queue will be the first item removed from the queue.
    A queue can be implemented using a list or a linked list.
```

Param


```python
    queue_list: list
        The list to initialize the queue with
    max_size: int
        The maximum size of the queue
```

Example


```python
    queue = Queue([1, 2, 3, 4, 5], 10)

    a = queue.dequeue()
    print(a)
```

Reference


```python
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
```




 <details>
<summary>

### >  > [function Queue.init](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueinit) 



</summary>

[def __init__(self, queue_list: list = None, max_size: int = None):](./../toolbox/queue_local.py#L30) 

Note


```python
        If the queue_list is not None, then the queue will be initialized with the list
        If the max_size is not None, then the queue will be initialized with the max_size
```

Param


```python
        queue_list: list
            The list to initialize the queue with
        max_size: int
            The maximum size of the queue
```

Return


```python
        None
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], 10)

        a = queue.dequeue()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.enqueue](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueenqueue) 



</summary>

[def enqueue(self, item):](./../toolbox/queue_local.py#L61) 

Note


```python
        Adds the item to the end of the queue
```

Param


```python
        item: any
            The item to add to the queue
```

Return


```python
        None
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.dequeue](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuedequeue) 



</summary>

[def dequeue(self):](./../toolbox/queue_local.py#L90) 

Note


```python
        Removes the first item from the queue
```

Param


```python
        None
```

Return


```python
        item: any
            The item that was removed from the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.dequeue()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.size](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuesize) 



</summary>

[def size(self) -> int:](./../toolbox/queue_local.py#L118) 

Note


```python
        Returns the size of the queue
```

Param


```python
        None
```

Return


```python
        size: int
            The size of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        print(queue.size())
```



</details>


 <details>
<summary>

### >  > [function Queue.is_empty](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueis_empty) 



</summary>

[def is_empty(self) -> bool:](./../toolbox/queue_local.py#L146) 

Note


```python
        Returns True if the queue is empty, False otherwise
```

Param


```python
        None
```

Return


```python
        is_empty: bool
            True if the queue is empty, False otherwise
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(queue.is_empty())
```



</details>


 <details>
<summary>

### >  > [function Queue.peek](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuepeek) 



</summary>

[def peek(self):](./../toolbox/queue_local.py#L173) 

Note


```python
        Returns the first item in the queue without removing it
```

Param


```python
        None
```

Return


```python
        item: any
            The first item in the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.peek()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.get_list](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueget_list) 



</summary>

[def get_list(self):](./../toolbox/queue_local.py#L201) 

Note


```python
        Returns the list of items in the queue
```

Param


```python
        None
```

Return


```python
        list: list
            The list of items in the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.get_list()
        print(a)
```



</details>


 <details>
<summary>

### >  > [function Queue.len](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuelen) 



</summary>

[def __len__(self):](./../toolbox/queue_local.py#L230) 

Note


```python
        Returns the size of the queue
```

Param


```python
        None
```

Return


```python
        size: int
            The size of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(len(queue))
```



</details>


 <details>
<summary>

### >  > [function Queue.copy](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuecopy) 



</summary>

[def copy(self):](./../toolbox/queue_local.py#L256) 

Note


```python
        Returns a copy of the queue
```

Param


```python
        None
```

Return


```python
        new_queue: Queue
            A copy of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.copy](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuecopy) 



</summary>

[def __copy__(self):](./../toolbox/queue_local.py#L288) 

Note


```python
        Returns a copy of the queue
```

Param


```python
        None
```

Return


```python
        new_queue: Queue
            A copy of the queue
```

Example


```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.eq](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueeq) 



</summary>

[def __eq__(self, other):](./../toolbox/queue_local.py#L317) 

Note


```python
        Returns True if the queues are equal, False otherwise
```

Param


```python
        other: Queue
            The other queue to compare to
```

Return


```python
        is_equal: bool
            True if the queues are equal, False otherwise
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue == other)
```



</details>


 <details>
<summary>

### >  > [function Queue.ne](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuene) 



</summary>

[def __ne__(self, other):](./../toolbox/queue_local.py#L348) 

Note


```python
        Returns True if the queues are not equal, False otherwise
```

Param


```python
        other: Queue
            The other queue to compare to
```

Return


```python
        is_not_equal: bool
            True if the queues are not equal, False otherwise
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue != other)
```



</details>


 <details>
<summary>

### >  > [function Queue.getitem](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuegetitem) 



</summary>

[def __getitem__(self, index):](./../toolbox/queue_local.py#L373) 

Note


```python
        Returns the item at the given index
```

Param


```python
        index: int
            The index of the item to get
```

Return


```python
        item: any
            The item at the given index
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue[2])
```



</details>


 <details>
<summary>

### >  > [function Queue.setitem](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuesetitem) 



</summary>

[def __setitem__(self, index, value):](./../toolbox/queue_local.py#L397) 

Note


```python
        Sets the item at the given index to the given value
```

Param


```python
        index: int
            The index of the item to set
        value: any
            The value to set the item to
```

Return


```python
        None
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue[2] = 10
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.delitem](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuedelitem) 



</summary>

[def __delitem__(self, index):](./../toolbox/queue_local.py#L423) 

Note


```python
        Deletes the item at the given index
```

Param


```python
        index: int
            The index of the item to delete
```

Return


```python
        None
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        del queue[2]
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.iter](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueiter) 



</summary>

[def __iter__(self):](./../toolbox/queue_local.py#L447) 

Note


```python
        Returns an iterator for the queue
```

Param


```python
        None
```

Return


```python
        iter: iter
            An iterator for the queue
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in queue:
            print(item)
```



</details>


 <details>
<summary>

### >  > [function Queue.reversed](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuereversed) 



</summary>

[def __reversed__(self):](./../toolbox/queue_local.py#L471) 

Note


```python
        Returns an iterator for the queue in reverse order
```

Param


```python
        None
```

Return


```python
        reversed: iter
            An iterator for the queue in reverse order
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in reversed(queue):
            print(item)
```



</details>


 <details>
<summary>

### >  > [function Queue.contains](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuecontains) 



</summary>

[def __contains__(self, item):](./../toolbox/queue_local.py#L495) 

Note


```python
        Returns True if the item is in the queue, False otherwise
```

Param


```python
        item: any
            The item to check for
```

Return


```python
        is_in: bool
            True if the item is in the queue, False otherwise
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(1 in queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.add](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueadd) 



</summary>

[def __add__(self, other):](./../toolbox/queue_local.py#L519) 

Note


```python
        Returns a new queue with the items from both queues
```

Param


```python
        other: Queue
            The other queue to add to this queue
```

Return


```python
        new_queue: Queue
            A new queue with the items from both queues
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        new_queue = queue + other
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.iadd](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueiadd) 



</summary>

[def __iadd__(self, other):](./../toolbox/queue_local.py#L550) 

Note


```python
        Returns this queue with the items from both queues
```

Param


```python
        other: Queue
            The other queue to add to this queue
```

Return


```python
        self: Queue
            This queue with the items from both queues
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        queue += other
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.mul](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuemul) 



</summary>

[def __mul__(self, other):](./../toolbox/queue_local.py#L578) 

Note


```python
        Returns a new queue with the items from this queue repeated the given number of times
```

Param


```python
        other: int
            The number of times to repeat the queue
```

Return


```python
        new_queue: Queue
            A new queue with the items from this queue repeated the given number of times
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        new_queue = queue * 3
        print(new_queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.imul](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queueimul) 



</summary>

[def __imul__(self, other):](./../toolbox/queue_local.py#L607) 

Note


```python
        Returns this queue with the items from this queue repeated the given number of times
```

Param


```python
        other: int
            The number of times to repeat the queue
```

Return


```python
        self: Queue
            This queue with the items from this queue repeated the given number of times
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue *= 3
        print(queue)
```



</details>


 <details>
<summary>

### >  > [function Queue.str](/docs/TOOLBOX-QUEUE_LOCAL.md#function-queuestr) 



</summary>

[def __str__(self):](./../toolbox/queue_local.py#L636) 

Note


```python
        Returns a string representation of the queue
```

Param


```python
        None
```

Return


```python
        string: str
            A string representation of the queue
```

Example


```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue)
```



</details>

</details>

<br></details>

