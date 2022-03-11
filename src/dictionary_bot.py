from sys import prefix
import discord
import os
import dotenv


class dictionary_bot(discord.Client):
    prefix = "$"

    async def on_ready(self):
        print(f"logged in as {self.user}")

    async def on_message(self, message):

        # Prevents the bot from responding to itself
        if message.author == self.user:
            return


        ####################
        ## Debug Commands ##
        ####################

        if message.content.startswith(prefix + "running"):
            await message.channel.send(f"Hello, {message.author}")


dotenv.load_dotenv()
token = os.environ["bot_token"]

bot = dictionary_bot()
bot.run(token)
