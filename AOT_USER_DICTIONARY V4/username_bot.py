# bot.py
import os
import bot_module as module
import usage_sheet as usage_sheet
import Chatlog_history
import discord
import json

#remove future warning that comes with pandas
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

import dataframe_image as dfi


from discord.ext.commands import CommandNotFound
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@bot.command(id='id', help="Find's player names when given an ID. Example: !id 0002cf8ba06e41e2b9eb4e8666a4ee6b")
async def id(ctx, id):
    user = ctx.message.author
    print(f"{user} requested an id!")
    #add usage by user to data
    usage_sheet.usage_dictionary(str(user), "id")
    names = module.find_names(id)
    if names:
        names = ', '.join(names)
        await ctx.send(f"```\nI found the names: {names}\n```")
    else:
        await ctx.send(f"```\nNo names found for that ID.\n```")

@bot.command(usage='usage', help="Shows how to use bot")
async def usage(ctx):
    user = ctx.message.author
    print(f"{user} requested usage data!")
    with open("Usage_data.json", "r")as file:
        usage_data = json.load(file)
        #print(json.dumps(usage_data, indent = 3))
        try:
            del usage_data[str(user)]["Names Contributed"]
        except Exception:
            pass
        #usage_data = usage_data[str(user)]
        if usage_data[str(user)]["lobby"] and usage_data[str(user)]["id"]:
            await ctx.send(f'```Your stats:\n!lobby: {usage_data[str(user)]["lobby"]}\n!id: {usage_data[str(user)]["id"]}```')
        elif usage_data[str(user)]["lobby"]:
            await ctx.send(f'```Your stats:\n!lobby: {usage_data[str(user)]["lobby"]}```')
        elif usage_data[str(user)]["id"]:
            await ctx.send(f'```Your stats:\n!lobby: {usage_data[str(user)]["id"]}```')

    
    #await ctx.send(f'```\n1. Type !id and an ID like this "!id 0002cf8ba06e41e2b9eb4e8666a4ee6b"\n'+
    #'\n\n2. Type !lobby and the copy and pasted data from typing the word "list" in console.'+
    #'\nEX:\n"!lobby \n<indent=2%>"poopooapg"  [000268c2306442fa950636a3b91985d1]</indent>'+
    #'<indent=2%>"[FR]Paranoia"  [000223906bb94a6791dff4153a72d01b]</indent>\n\n```')

@bot.command(helpvid='helpvid', help="Shows how to use bot with a vid!")
async def helpvid(ctx):
    await ctx.send('https://www.youtube.com/watch?v=MVRpFt5hjoI&t=2s')


@bot.command(lobby='lobby', help="Find's lobby info.")
async def lobby(ctx, *, args):

    paste = ''.join(args[:])

    user = ctx.message.author
    print(f"{user} sent lobby data!")
    #add usage by user to data
    usage_sheet.usage_dictionary(str(user), "lobby")
   
    #return dictionary from get paste module
    return_dict, names_added = module.get_paste(paste)

    #WE MAKE FRAME BOYO
    return_frame = pd.DataFrame.from_dict(return_dict, orient='index', columns=[f"{user}'s Lobby Info:"])
    return_frame.fillna("",inplace=True)

    return_frame = return_frame.style.set_properties(**{
                                       'color': 'teal',
                                       'border-color': 'white'})

    dfi.export(return_frame, 'Lobby_Response.png')
    
    try:
        await ctx.message.delete()
    except Exception:
        pass
    #await ctx.send(embed=embed)
    await ctx.send(file=discord.File('Lobby_Response.png'))
    
    for i in range(1, names_added+1):
        usage_sheet.usage_dictionary(str(user), "Names Contributed")
    

@bot.command(update='update', help="Updates database.")
async def update(ctx):
    
    await ctx.send(f"```\nUpdating with chatlog files.\n```")
    
    Chatlog_history.update_history()
    Chatlog_history.get_current_chatlog()
    
    await ctx.send(f"```\nUpdated!\n```")

bot.run(TOKEN)