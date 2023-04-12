import discord
from ai import answerGpt
from envVars import discordKey

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.content.startswith('$hello'):
            await message.channel.send(f"Witaj wędrowcze {message.author}. Pierdolniesz kieliha za spokój moich zmarłych druhów?")

        if message.content.startswith('$gpt'):
            await message.channel.send(f"Odpowiadam na pytanie: {message.content[5:]}")
            answer = answerGpt(message.content[5:])
            await message.channel.send(f"{answer}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discordKey)