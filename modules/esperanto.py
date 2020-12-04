import requests
import json
body = {"owner_email": "cli+test1@company.com", "salesforce_id": "0011s000007ZA3cAAG",
        "company_url": "https://www.company.com", "api_access": True, "api_limit": 100.0,
        "contract_end_date": "2019-12-19", "data_sharing": "Esperanto Only", "connections": 2.0,
        "contract_start_date": "2019-12-31", "impressions": 1.0, "user_seats": 3.0,
        "account_name": "company Esperanto Test"}

headers = {"Content-Type": "application/json", "Authorization": "UAALRTDEERBR3PRNKUZIAHBSOU"}
url="https://security-stag.libring.com/v1/contract"
data=json.dumps(body)
response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.content)

js={"hello":"thank you"}
data1=json.dumps(js)
data2=json.dumps(data1)
print(data1)
print(data2)