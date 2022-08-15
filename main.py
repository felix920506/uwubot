import discord
import random

with open('token.txt','r',encoding='utf8') as tokenfile:
    token = tokenfile.read().strip()

bot = discord.Bot(prefix='')

class view1(discord.ui.View):

    def __init__(self,style):
        super().__init__()
        if style == 1:
            self.children[0].style = discord.ButtonStyle.primary
        elif style == 2:
            self.children[0].style = discord.ButtonStyle.secondary
        elif style == 3:
            self.children[0].style = discord.ButtonStyle.success
        elif style == 4:
            self.children[0].style = discord.ButtonStyle.danger

    @discord.ui.button(label = 'uwu')
    async def buttonclicked(self,button,interaction):
        await interaction.response.send_message(view=view1(random.randint(1,4)))

@bot.event
async def on_ready():
    print('ready')

@bot.command(description='uwu')
async def uwu(ctx):
    await ctx.respond(view=view1(random.randint(1,4)))

bot.run(token)