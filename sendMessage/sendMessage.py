from telethon.sync import TelegramClient, events
from telethon.tl.types import InputPeerUser
import os 
import json
from dotenv import load_dotenv

load_dotenv('../.env')


api_id = os.environ['api_id'] 
api_hash = os.environ['api_hash']
phone = os.environ['phone']
username = os.environ['username']
api_hash = str(api_hash)

message = 'your message here...'


with TelegramClient('name', api_id, api_hash) as client:
      client.send_message('me' , message)  ; 
      path = '../data'
      for folder in os.listdir(path):
            folder_path = os.path.join(path , folder )
            for filename in os.listdir(folder_path):
                  full_filename_path = os.path.join(folder_path , filename)
                  file = open( full_filename_path ,'r')
                  users = json.loads(file.readlines()[0])
                  for user in users:
                        # messages = client.get_message_history( InputPeerUser( user[0] , int(user[1]) )  )
                        # if len(message) > 1:
                        #       continue
                        
                        client.send_message( InputPeerUser( user[0], int(user[1])) , message )
                  print('Done sending file: %s'%(full_filename_path))
      client.run_until_disconnected()

