# Script for autmating fetching and sending messages to members in certin groups
# first install Python 3.10.9
# then run the following commands:
    pip install telethon
    pip install python-dotenv
# then
# write your telegram info in the .env file
# to get the api_id & api_hash visit : https://my.telegram.org/auth enter your phone then click API development tools and create an instance 

# then find telegram groups with hidden members and put them in (groups_with_hidden_memebers.json)
# then find telegram groups with public members and put them in (groups_with_public_memebers.json)

# write your messsage in sendMessage.py file 
# then run:
    python get_users.py  
    # it will ask for your phone number
    # wait for it , it will take some time
# finally run:
    cd sendMessage & python sendMessage.py
 
## note: there is some limitations on using this (you can send 20 message every 5 minutes)
## script needs to be edited to sleep for 5 minutes each 20 message ..