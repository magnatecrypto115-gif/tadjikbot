# -*- coding: utf-8 -*-
import random
import discord


zov = ["иди нахуй ", "я твой рот ебал ", "чтоб ты сдох ", "я твою маму ебал "]
xyecoc = ["чурка", "чурбан", "жид", "таджик", "хач", "хохол", "кацап"]
message_counter = 0

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot started as", self.user)

    async def on_message(self, message):
        global message_counter
        if message.author == self.user:
            return

        message_counter += 1

        target = random.randint(5, 10)

        if message_counter >= target:
            await message.channel.send(random.choice(zov) + random.choice(xyecoc))
            message_counter = 0 


client = MyClient(intents=intents)
client.run("MTQ0NjQ0NTI3MTAyOTY0NTM0Mg.Gqa_Tk.T6MFIjKM54kpIJQyBj6VuxGV0tequZLcap8PfM")
