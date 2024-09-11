import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
# Crear una instancia del bot con un prefijo
bot = commands.Bot(command_prefix='$', intents=intents)
import os
print(os.listdir('Imagenes'))
list_memes = os.listdir('Imagenes')

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
@bot.command(name='clasificacion')
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

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command(name='ima')
async def ima(ctx, animal: str):
    imagenes = {
        "loro": "Loro.jpeg",
        "mapache": "Mapache.jpeg",
        "oveja": "Oveja.jpeg",
    }
    imagen = imagenes.get(animal.lower(), None)
    if imagen:
        with open(f'Imagenes/{imagen}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("No tengo imagen para ese animal.")

@bot.command(name='imagenaleatoria')
async def imagenaleatoria(ctx):
    select_ima = random.choice(list_memes)
    with open(f'Imagenes/{select_ima}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
# Ejecutar el bot
bot.run("")
