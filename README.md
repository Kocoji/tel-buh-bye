# Requirement & How to
- Clone this repo:
  - `git clone https://github.com/Kocoji/tel-buh-bye.git`
- Python3 & Linux (I have not tested on Windows env)
- Install the packages in the `requirements.txt` file 
  - `pip3 install -r requirements.txt`
- Get the API From [Telegram](https://my.telegram.org/), (Quote from https://docs.telethon.dev/en/stable/basic/signing-in.html)
> Before working with Telegram’s API, you need to get your own API ID and hash:
> - Login to your Telegram account with the phone number of the developer account to use.
> - Click under API Development tools.
> - A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
> - Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!
- Create the env variable: 
  - E.g. `export API_ID='12345678' API_HASH='d0d46c372ff1f1522434951a2b3c4d'`
  - Or, create the file include 2 vars: `API_ID='12345678' API_HASH='d0d46c372ff1f1522434951a2b3c4d'`, then, from the shell: type `. thefilename`

# Docker
You can build the image that included in this source. E.g. `docker build . -t buhbye`

Or, you can pull the image from my Docker Hub: `docker pull kocoji/buhbye`
- Run it (Sample commands, remember to replace your env variables!):
  - `getlist` cmd: `docker run --rm -it -v $(pwd)/data:/usr/src/app/data -e API_ID=12345678 -e API_HASH='daae74e0549286ae54b4d60c8b9a6c89a' buhbye getlist`
  - `bye` cmd: `docker run --rm -it -v $(pwd)/data:/usr/src/app/data -e API_ID=12345678 -e API_HASH='daae74e0549286ae54b4d60c8b9a6c89a' buhbye bye --force`

# Commands
Currently, this script has 2 commands:
- `getlist`
  - to get the list of group chats & channels that you have joined, then save to the `whitelist.txt` file
  - Edit the file and keep the room you want to stay in.
  - the `bye` command read the name of group chat that saved in `whitelist.txt` as the whitelist, so edit and save the name of group/channel you want to keep in this file only. 
- `bye`:
  - if you run this one command without run/update the `getlist` whitelist file. You will leave all groups/channels 
  - use `--force` to run in the unattend mode.
