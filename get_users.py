import json
import asyncio
import os
from datetime import date, datetime
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)
from dotenv import load_dotenv



load_dotenv('.env')


api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
phone = os.environ['phone']
username = os.environ['username']
api_hash = str(api_hash)



client = TelegramClient(username, api_id, api_hash)
public_channels_json = open('groups_with_public_members.json' , 'r' ).readlines()[0]
hidden_channels_json = open('groups_with_hidden_members.json' , 'r' ).readlines()[0]

public_channels = json.loads(public_channels_json)
hidden_channels = json.loads(hidden_channels_json)


async def get_public(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    # main logic
    counter = 0  
    for channel in public_channels:
        user_input_channel = channel['url']

        if user_input_channel.isdigit():
            entity = PeerChannel(int(user_input_channel))
        else:
            entity = user_input_channel

        my_channel = await client.get_entity(entity)

        offset = 0
        limit = 100
        all_participants = []

        while True:
            participants = await client(GetParticipantsRequest(
                my_channel, ChannelParticipantsSearch(''), offset, limit,
                hash=0
            ))
            if not participants.users:
                break
            all_participants.extend(participants.users)
            offset += len(participants.users)

        all_user_details = []
        for participant in all_participants:
            all_user_details.append([participant.id , participant.access_hash])
        
        with open('data/public/%d.json'%(counter), 'w') as outfile:
            json.dump(all_user_details, outfile)
        print('channel: %d done'%(counter) )
        counter+=1
        



async def get_hidden(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))
    # main logic
    counter = 0  
    for channel in hidden_channels:
        user_input_channel = channel['url']
        
        if user_input_channel.isdigit():
            entity = PeerChannel(int(user_input_channel))
        else:
            entity = user_input_channel

        my_channel = await client.get_entity(entity)

        all_messages = set()
        offset_id = 0
        limit = 100
        total_messages = 0
        total_count_limit = 0

        while True:
            print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
            history = await client(GetHistoryRequest(
                peer=my_channel,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                
                message = message.to_dict()
                print('from_id',message.get('from_id'))
                if message.get('from_id') == None or message.get('from_id').get('user_id') == None:
                    continue
                user_id =message['from_id']['user_id']
                peer = await client.get_input_entity(user_id)
                peer_ =(
                    peer.user_id,
                    peer.access_hash
                )
                # message['peer'] = peer_ 
                all_messages.add(peer_)
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break
            
        with open('data/hidden/%d.json'%(counter), 'w') as outfile:
            json.dump(list(all_messages) , outfile )


with client:
    client.loop.run_until_complete(get_public(phone))
    client.loop.run_until_complete(get_hidden(phone))
