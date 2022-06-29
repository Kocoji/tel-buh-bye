This code is used to leave the group and channel that i have joined.

# Requirement & How to
- Clone this repo
  - git clone https://github.com/Kocoji/tel-buh-bye.git
- python3 
- the packages in the `requirements.txt` file 
  - `pip3 install -r requirements.txt`
- Get the API, (Quote from https://docs.telethon.dev/en/stable/basic/signing-in.html)
> Before working with Telegram’s API, you need to get your own API ID and hash:
> - Login to your Telegram account with the phone number of the developer account to use.
> - Click under API Development tools.
> - A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
> - Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!
- Create the env variable: 
  - e.g. `export api_id='12345678' api_hash='d0d46c372ff1f1522434951a2b3c4d'`
  - or, create the file include 2 vars: `api_id='12345678' api_hash='d0d46c372ff1f1522434951a2b3c4d'`, then, from the shell: type `. thefilename`

# Commands
- Currently, this code has 2 commands:
  - `getlist`
    - to get the list of group chats & channels that you have joined, then save to the `grouplist.txt` file
    - Edit the file and keep the room you want to stay in.
    - the `bye` command read the name of group chat that saved in `grouplist.txt` as the whitelist, so edit and save the name of group/channel you want to keep in this file only. 
  - `bye`:
    - if you run this one command without run/edit the `getlist` whitelist file. You will leave all groups/channels 
    - use `--force` to run in the unattend mode.

# Problems.
- You might be get the error from Telegram similar the below:
`telethon.errors.rpcerrorlist.FloodWaitError: A wait of 246 seconds is required (caused by DeleteChatUserRequest)`
  - solution: wait until the telegram unblock you