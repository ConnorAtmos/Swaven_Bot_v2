import discord
from discord.ext import commands

class discordBot:
    def __init__(self, api_token: str) -> None:
        """
        Parameters
        ----------
        api_token : str
            The API token of the Discord Bot

        Returns
        -------
        None

        Notes
        -----
        This class is used to create a Discord Bot.

        References
        ----------
        https://docs.pycord.dev/en/stable/

        Examples
        --------
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.run()
        """
        intents = discord.Intents.all()
        self.bot = commands.Bot(intents=intents)
        self.api_token = api_token
        self.guild_ids = []

    def add_server_id(self, server_id: int) -> None:
        """
        Parameters
        ----------
        server_id : int
            The ID of the server to add the bot to

        Returns
        -------
        None

        Notes
        -----
        This function is used to add a server ID to the bot.

        References
        ----------
        https://docs.pycord.dev/en/stable/

        Examples
        --------
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.add_server_id(123456789)

        @bot.bot.slash_command(name="hello", guild_ids=bot.guild_ids)
        async def hello(ctx, name: str = "World"):
            await ctx.send(f"Hello {name}!")

        bot.run()
        """
        self.guild_ids.append(server_id)

    def add_server_ids(self, server_ids: list) -> None:
        """
        Parameters
        ----------
        server_ids : list
            The IDs of the servers to add the bot to

        Returns
        -------
        None

        Notes
        -----
        This function is used to add a list of server IDs to the bot.

        References
        ----------
        https://docs.pycord.dev/en/stable/

        Examples
        --------
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        server_ids = [123456789, 987654321]
        bot.add_server_ids(server_ids)

        @bot.bot.slash_command(name="hello", guild_ids=bot.guild_ids)
        async def hello(ctx, name: str = "World"):
            await ctx.send(f"Hello {name}!")


        bot.run()
        """
        self.guild_ids.extend(server_ids)

    def add_slash_command_group(self, slash_command_group) -> None:
        """
        Parameters
        ----------
        slash_command_group
            The IDs of the servers to add the bot to.

        Returns
        -------
        None

        Notes
        -----
        This function is used to add a list of server IDs to the bot.

        References
        ----------
        https://docs.pycord.dev/en/stable/

        Examples
        --------
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
        """
        self.bot.add_application_command(slash_command_group)

    def run(self) -> None:
        """
        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This function is used to run the Discord Bot.

        References
        ----------
        https://docs.pycord.dev/en/stable/

        Examples
        --------
        from discord_bot import discordBot
        api_token = "YOUR_API_TOKEN"
        bot = discordBot(api_token)
        bot.run()

        """
        print("Running Discord Bot...")
        print("To stop the bot, Press Ctrl+C")
        self.bot.run(self.api_token)

