[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import discord_bot`

Alternative Import Statement: `from toolbox.discord_bot import *`

# >  class discordBot #

### [class discordBot:](./../toolbox/discord_bot.py#L4) 

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

#### Functions and Classes

</summary>

# >  >  function discordBot.init #

### [def __init__(self, api_token: str) -> None:](./../toolbox/discord_bot.py#L5) 

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

# >  >  function discordBot.add_server_id #

### [def add_server_id(self, server_id: int) -> None:](./../toolbox/discord_bot.py#L36) 

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

# >  >  function discordBot.add_server_ids #

### [def add_server_ids(self, server_ids: list) -> None:](./../toolbox/discord_bot.py#L70) 

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

# >  >  function discordBot.add_slash_command_group #

### [def add_slash_command_group(self, slash_command_group) -> None:](./../toolbox/discord_bot.py#L106) 

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

# >  >  function discordBot.run #

### [def run(self) -> None:](./../toolbox/discord_bot.py#L151) 

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

