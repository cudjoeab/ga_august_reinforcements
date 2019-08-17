import requests
import json 

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
body = json.loads(ottawa_wards_response.content)

 
# 1. Iterate through your new dictionary 
# and display the name of each ward in the collection.
for i in range(len(body['objects'])):
    print(body['objects'][i]['name'])

print('') 

