import asyncio
import os
from telethon import TelegramClient
from telethon import utils
from typing import Optional
from functools import wraps
import typer

# Use your own values from my.telegram.org
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
client = TelegramClient('session2', api_id, api_hash)

filename = "grouplist.txt"

app = typer.Typer()

def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapper

@app.command()
@coro
async def getlist():
    await asyncio.sleep(1)  
    async with client:      
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                typer.echo(dialog.name)
                with open(filename, "a") as file:
                    file.write(dialog.name + "\n")   

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
                        print("Bye ",dialog.name)
                        await dialog.delete()
    else:
        typer.echo("Operation cancelled")

if __name__ == "__main__":
    app()
