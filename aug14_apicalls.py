import requests
import json 

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
body = json.loads(ottawa_wards_response.content)
# print(body["name"]) 

print(ottawa_wards_response.json())
