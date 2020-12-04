import json

data = {
    "impressions_sum": 123,
    "connections_sum": 456
}

print(json.dumps(data))

import requests

res=requests.post("https://www.libring.com/mayun/shabi",data=b"fucker")
print(res.content)
print(res.status_code)
res.raise_for_status()

