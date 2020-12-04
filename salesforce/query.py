import requests
import json

headers = {"Content-Type": "application/x-www-form-urlencoded"}
url = "https://test.salesforce.com/services/oauth2/token"
body = {"grant_type": "password",
        "client_id": "3MVG9pcaEGrGRoTK5RVMemYU9HdY4QwF0GfIS26F1cFnT2exV6M.X__hYgGn7ZrUgiUv3XBX8OgeMgMSmzO9k",
        "client_secret": "E590EF121AC603079A6648F700826B4256BC2ADD21BF375A0E66CF892A6A07E9",
        "username": "",
        "password": "Hello2020!@"
        }
# Acquire Token
response = requests.post(url, headers=headers, data=body)
print(response.status_code)
print(response.content)
js = json.loads(response.content)
token, host_url = js.get("access_token"), js.get("instance_url")

# SOQL
sql = """
SELECT Account__c,Account__r.Owner.Email FROM Provisioning__c
"""

url = host_url + "/services/data/v47.0/query/?q=" + sql
headers = {
    "Authorization": "Bearer " + token,
    "CONTENT-TYPE": "APPLICATION/JSON"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.content)

data=json.loads(response.content)
records=data["records"]
# print(records)
print("----------- records -------------")
print(records[1])