import discord
from discord.ext import commands
import bilgi

TOKEN = bilgi.TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name="kick")
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.name} adlı kişi bu sunucudan atıldı.')

@bot.command(name="ban")
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'{member.name} adlı kişi bu sunucudan yasaklandı.')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Eğer mesajda küfür varsa, mesajı sil ve uyarı gönder
    f = open('C:\Visual Studio Code Projeleri\Python\Kodland\Python Pro\M2L2\kufur.txt', 'r', encoding='utf-8')
    kufurler = f.read().splitlines()
    for kufur in kufurler:
        if kufur in message.content.lower():
            await message.delete()
            msg = f'{message.author.mention}! Kufur edeni tinkywinkylerim aklin basina gelir!'
            await message.channel.send(msg)



bot.run(TOKEN)
    
