import discord
import random  
from discord.ext import commands

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def hello(ctx):
    await ctx.send("hi")
@bot.event    
async def bye(ctx):
    await ctx.send("see you soon")

@bot.command()
async def joined(ctx, member: discord.Member):
    
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


# Reemplaza "Your_Token_Here" con el token real de tu bot
bot.run("")
