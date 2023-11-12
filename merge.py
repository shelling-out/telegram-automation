import json
import os

def convert_to_array(public_set):
    public = []
    for i in public_set:
        public.append(i)
    return public

public = set()

path = 'data'
for json_file in os.listdir('data\public'):
    file_path = os.path.join( path ,'public' , json_file)
    file = open(  file_path , 'r')
    json_content = file.readlines()[0]
    content = json.loads(json_content)
    for user in content:
        public.add((user[0],user[1]))

public = convert_to_array(public)
file = open('data/public/all_users.json','w')
json_content = json.dumps(public) 
file.writelines(json_content)
