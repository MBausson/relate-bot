import discord
from discord.ext import commands
import sys
import translate

# The program is launched with the bot's token as parameter. The token might not be the 2nd parameter, please adapt the line below if needed.
TOKEN = sys.argv[1]
client = commands.Bot(command_prefix='>', intents=discord.Intents.all(), case_insensitive=True)


@client.command()
async def lang(ctx, lang: str=None, *, args=None):
    if lang is None:
        lang = 'en'
        
    elif lang not in translate.languages:
        await ctx.send(f'{ctx.author.mention} Please enter a supported language code (ex: `en`, `fr`, `es`)')
        return

    userold = translate.get_user(int(ctx.author.id))

    if userold is None:
        translate.add_user(int(ctx.author.id), lang)
        return

    translate.change_user(int(ctx.author.id), oldlang=userold['lang'], newlang=lang)
    await ctx.send(f'{ctx.author.mention} The messages will now be **translated** to you in `{lang}` :)')


@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji != '🔤':
        return

    userold = translate.get_user(int(user.id))
    try:
        if userold is None:
            await user.send(translate.translate(reaction.message.content, 'en'))
        else:
            await user.send(translate.translate(reaction.message.content, userold['lang']))

    except discord.Forbidden:
        await reaction.message.channel.send(f"{user.mention} I can't DM you! Did you block me ?")

    #   Remove the reaction added
    await reaction.remove(user)


@client.event
async def on_ready():
    print('-----#-----#-----')
    print(f'Logged in as {client.user}')
    print(f'Discord.py version: {discord.__version__}')
    print(f'Python version: {sys.version}')
    print('-----#-----#-----')

client.run(TOKEN)
