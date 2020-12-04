#
# for i in {"123":"234","456":"789"}.items():
#     print(type(i),i)
#
#
# if (123,"231")==(123,"231"):
#     print(2)
#
#
# def work():
#     hello=1+1
#     return
#
#
# print(work())
#
# import json
# import urllib2
#
# data={"hello":"world"}
# try:
#     url="http://127.0.0.1:6001/response"
#     data = json.dumps(data)
#     req = urllib2.Request(url, headers={"CONTENT-TYPE": "APPLICATION/JSON"}, data=data)
#     urllib2.urlopen(req)
# except Exception as e:
#     for i in dir(e):
#         pass
#
# from urllib2 import HTTPError
# HTTPError(404)
# response = .read(
# print(response)
import json
import datetime

js = {
"salesforce_id":123456,
"start_time":"2019-10-10 0:0:0",
"end_time":"2019-10-11 0:0:0"
}
js = {
"impressions_sum":1200,
"connections_sum":10,
}

js={"salesforce_id":[
    "123456",
    "123457",
    "123458",
    "123459",
    "123460",
    "123461"
]}
print(json.dumps(js))

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#
# js={}
# js["hellp"]
js = [
    {"salesforce_id": "123456ABC",
     "account_name": "",
     "owner_email": "owner@.com",
     "data_sharing": "None",
     "impressions": 70,
     "connections": 20,
     "user_seats": 10,
     "api_access": True,
     "api_limit": 50,
     "company_url": "https://salesforce.com/a",
     "contract_start_date": "2019-10-01",
     "contract_end_date": "2020-10-01"},

    {"salesforce_id": "123456ABD",
     "account_name": "",
     "owner_email": "owner2@.com",
     "data_sharing": "None",
     "impressions": 70,
     "connections": 20,
     "user_seats": 10,
     "api_access": True,
     "api_limit": 50,
     "company_url": "https://salesforce.com/",
     "contract_start_date": "2019-10-01",
     "contract_end_date": "2020-10-01"}
]

js = json.dumps(js)
print(js)
