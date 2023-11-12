## Script for automating sending messages to members in certain groups.
### 1.  Environment setup
	1. install Python 3.10.9
	2. then run the following commands:
	  >pip install telethon
	    pip install python-dotenv
### 2.  then write your telegram info in the .env file
> to get the api_id & api_hash visit : https://my.telegram.org/auth enter your phone then click API development tools and create an instance 

### 3. then get the  telegram groups with hidden members and put them in (groups_with_hidden_memebers.json)
### 4. then find telegram groups with public members and put them in (groups_with_public_memebers.json)

### 5. write your messsage in sendMessage/sendMessage.py file 
### 6. then run:
    python get_users.py  
   it will ask for your phone number
   wait for it , it will take some time
### finally run:
     cd sendMessage & python sendMessage.py
 
### Note: there is some limitations on using this (you can send 20 message every 5 minutes)
### todo: script needs to be edited to sleep for 5 minutes each 20 message ..
