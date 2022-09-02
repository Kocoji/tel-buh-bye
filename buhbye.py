#!/usr/bin/env python3
import asyncio, os, time
from telethon import TelegramClient
from telethon import utils
from telethon import errors
from typing import Optional
from functools import wraps
import typer

# Use your own values from my.telegram.org
path= "./data"
filename = path +"/whitelist.txt"
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient(path + '/session', api_id, api_hash)

app = typer.Typer()

def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapper

def exists(str):
    return os.path.exists(str)

@app.command()
@coro
async def getlist():
    await asyncio.sleep(1)
    if exists(path): 
        pass
    else:
        os.mkdir(path)

    if exists(filename):
        os.remove(filename)

    async with client:   
        count = 0   
        typer.echo("Running")
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                count += 1
                with open(filename, "a") as file:
                    file.write(dialog.name + "\n")   
        typer.echo("Done! Found {} groups and channels!".format(count))
        if exists(filename):
            typer.echo("Please check the whitelist.txt in ./data folder")
            os.chmod(filename, 0o777)

@app.command()
@coro
async def bye(force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to leave ALL group/channel?",
        help="Force deletion without confirmation.",
    )):
    await asyncio.sleep(1)
    """
    Leave ALL group that you have joined.

    If --force is not used, will ask for confirmation.
    """
    if force:        
        try:
            with open(filename) as file:
                whiteList = [line.rstrip() for line in file]
        except FileNotFoundError:
            whiteList = []
        async with client:      
            async for dialog in client.iter_dialogs():
                if dialog.is_group or dialog.is_channel:
                    isDel = True
                    for list in whiteList:
                        if dialog.name == list:
                            isDel = False
                            print("Don't delete ",dialog.name)
                            break
                    if isDel:
                        try:
                            print("Bye ",dialog.name)
                            await dialog.delete()
                        except errors.FloodWaitError as e:
                            print('Have to sleep', e.seconds, 'seconds')
                            time.sleep(e.seconds)
    else:
        typer.echo("Operation cancelled")

if __name__ == "__main__":
    app()
