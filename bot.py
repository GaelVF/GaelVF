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
    print('Hemos iniciado sesión como {bot1}')

@bot.command()
async def hello(ctx):
    await ctx.send("hi")

@bot.command()    
async def bye(ctx):
    await ctx.send("see you soon")

@bot.command()
async def joined(ctx, member: discord.Member):
    
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)  
async def spam(ctx):
    await ctx.send("¡No hagas spam!")

# Manejo de excepciones para comandos que no existen
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Este comando no existe. Por favor, intenta con otro.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Parece que faltan argumentos. Verifica el comando e intenta de nuevo.')
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Este comando está en cooldown. Intenta de nuevo en {round(error.retry_after, 2)} segundos.')
    else:
        # Loguea cualquier otro error que no sea manejado específicamente
        print(f'Ocurrió un error: {error}')
        await ctx.send('Ocurrió un error inesperado. Por favor, intenta de nuevo más tarde.')

bot.run("")
