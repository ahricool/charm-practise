import requests

# https://test.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9pcaEGrGRoTK5RVMemYU9HdY4QwF0GfIS26F1cFnT2exV6M.X__hYgGn7ZrUgiUv3XBX8OgeMgMSmzO9k&client_secret=E590EF121AC603079A6648F700826B4256BC2ADD21BF375A0E66CF892A6A07E9&username=huazhang@company.com.esperanto&password=Aa123456' \
# -H 'Authorization: Bearer 00D1s0000008aV6!AQcAQKgjimDTeCqFoBQztASC6fIzinskl8puMGYC1nsBGlcLogwXe14VF4C3YWnzAZMpHf7Qgostu7pzUckm9SV.aeki29ax' \
#


headers = {"Content-Type": "application/x-www-form-urlencoded"}
url = "https://test.salesforce.com/services/oauth2/token"
body = {"grant_type": "password",
        "client_id": "3MVG9pcaEGrGRoTK5RVMemYU9HdY4QwF0GfIS26F1cFnT2exV6M.X__hYgGn7ZrUgiUv3XBX8OgeMgMSmzO9k",
        "client_secret": "E590EF121AC603079A6648F700826B4256BC2ADD21BF375A0E66CF892A6A07E9",
        "username": "cli@company.com.esperanto",
        "password": "Hello2020!@"
        }

response = requests.post(url, headers=headers, data=body)
print(response.status_code)
print(response.content)
import json

provision_id="124124124"
js = json.loads(response.content)
token, host_url = js.get("access_token"), js.get("instance_url")
url = host_url + "/services/data/v47.0/sobjects/" + "Provisioning__c/"+provision_id
headers = {
    "Authorization": "Bearer " + token,
    "CONTENT-TYPE": "APPLICATION/JSON"
}
print(headers)
# Ascend usage update boady
# body = {
#     "Date__c": "2019-10-01",
#     "ConnectionsSum__c": 19029,
#     "ImpressionsSum__c": 67890,
#     # "AccountID__c":"0011s000007ZA3cAAG",
#     "AccountID__c": "123sasdasdw9090iGH",
#     "UniqueLabel__c": "0011s000007ZA3cAAG 2019-11-02"
# }

# Provision status update body
body = {
    "Provisioning_status__c": "Active",
}
response = requests.patch(url, headers=headers, data=json.dumps(body))
print(response.status_code)
print(response.content)

# url=host_url+'/services/data/v47.0/query/?q=%s'
#
# if response.status_code==400:
#     print("Replace")
#     res=json.loads(response.content)[0]
#     record_id=res.get("message").split(" ")[-1]
#     print(record_id)
#
#     url = host_url + "/services/data/v32.0/sobjects/Usageb__c/"+record_id
#     body={
#     "ConnectionsSum__c":19029,
#     "ImpressionsSum__c":67890,
#     }
#
#     response=requests.patch(url,headers=headers,data=json.dumps(body))
#     print(url)
#     print(response.status_code)
#     print(response.text)
#

ct=response.text
if "The requested resource does not exist" in ct:
    print("hello")