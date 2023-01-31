import discord
 
from discord.ext import commands
 
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="y ayudando a las personas"))
 
@bot.event
async def on_ready():
    print(f"El bot {bot.user} está listo :)")

@bot.tree.command(name="test", description="Conoce tu tipo de aprendizaje")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.psicoactiva.com/test/educacion-y-aprendizaje/test-de-estilos-de-aprendizaje/", ephemeral=True)

@bot.command()
async def holis(ctx):
    await bot.tree.sync()
    await ctx.send("Ok Listo")

@bot.command()
async def nuevoembed(ctx):
    embed = discord.Embed(title="Konichiwa", description="Soy un bot multiusos, siéntete cómodo con mi uso", color=discord.Color.light_grey())
    embed.add_field(name="Usa el comando /test", value="Aparecerá un test funcional para tus tareas", inline=False)
    embed.add_field(name="Te quiero mucho", value="No te olvides de tomar agua :)", inline=True)
    embed.add_field(name= "Mira algo lindo", value= "Toca [aquí](https://youtube.com/shorts/ls3j4xvaddo?feature=share) para ver algo muy bonis uwu", inline=True)
    embed.set_author(name=ctx.message.author)
    embed.set_thumbnail(url= "https://cdn.discordapp.com/avatars/1067628661152432128/dd3ffa07d15aa07cbd7980fa61c7decb.png?size=2048")
    embed.set_image(url= "https://media2.giphy.com/media/TfcxUfi5ljpgvLleF4/giphy.gif?cid=6c09b9522f84fca06056e036a03195e952127faae12400e2&rid=giphy.gif&ct=s")
    embed.set_footer(text= "Fierro pariente")
    await ctx.send(embed=embed)

bot.run("token")
