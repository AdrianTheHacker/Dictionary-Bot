from sys import prefix
import discord
import os
import dotenv

from get_definition import get_def, get_def_num

class dictionary_bot(discord.Client):
    prefix = "!"

    def get_word(self, message):
        wordList = message.content.split()

        return wordList[1]

    async def on_ready(self):
        print(f"logged in as {self.user}")

    async def on_message(self, message):

        # Prevents the bot from responding to itself
        if message.author == self.user:
            return


        ####################
        ## Debug Commands ##
        ####################

        if message.content.startswith("!running"):
            await message.channel.send(f"Hello, {message.author}")
            print(f"Hello, {message.author}")

            return

        
        ###################
        ## Main Commands ##
        ###################

        if message.content.startswith("!define"):
            for definition in range(get_def_num(self.get_word(message))):
                await message.channel.send(f"{definition + 1}. {get_def(self.get_word(message), definition)}")

            return


dotenv.load_dotenv()
token = os.environ["bot_token"]

bot = dictionary_bot()
bot.run(token)
