import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
# Crear una instancia del bot con un prefijo
bot = commands.Bot(command_prefix='$', intents=intents)

# Diccionario con consejos para reducir residuos
consejos = [
    "Lleva una botella reutilizable a la escuela.",
    "Utiliza envases reutilizables para tu almuerzo.",
    "Reutiliza frascos de vidrio para guardar cosas.",
   
]

# Diccionario que clasifica objetos en reciclables o no reciclables
clasificacion_residuos = {
    "papel": "reciclable",
    "botella de plástico": "reciclable",
    "lata": "reciclable",
}

# Comando para recibir un consejo
@bot.command(name='consejo')
async def consejo(ctx):
    await ctx.send(random.choice(consejos))

# Comando para clasificar residuos
@bot.command(name='clasificar')
async def clasificar(ctx, *, objeto):
    objeto = objeto.lower()
    categoria = clasificacion_residuos.get(objeto, "No tenemos información sobre este objeto.")
    await ctx.send(f"El objeto '{objeto}' es {categoria}.")

# Comando para recibir un desafío
@bot.command(name='reto')
async def reto(ctx):
    await ctx.send("Hoy, trata de reducir tu uso de plásticos en al menos un 50%.")

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f"{bot.user.name} está listo y conectado.")

# Ejecutar el bot
bot.run("")