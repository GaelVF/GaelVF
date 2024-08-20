import discord 
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

# Lista de emojis

emojis = ['😀', '😂', '🥳', '😎', '😅', '😉', '😇', '😜', '👍', '🎉']

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$bye'):
        await message.channel.send("see you soon")
    elif message.content.startswith('$emoji'):
        await message.channel.send(random.choice(emojis))
    else:
        await message.channel.send(message.content)

client.run()
