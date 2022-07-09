import requests
import json

# url = "http://aa-conn-iaa-go-service.stg-feature.company.org:8888/v1/query"
url = "http://prod-aa-conn-iaa-go-service-t-internal.company.org/v1/query"

queries = [{'order_by': ['date', 'asc'], 'dimensions': ['device_code'],
        'metrics': ['active_devices', 'active_last_30_days', 'sessions'], 'meta': {},
        'filters': {'device_code': ['iPhone', 'iPad', 'iPod', 'AppleTV'], 'user_product_ids': [6900268],
                    'start_date': '2020-03-20', 'end_date': '2020-04-18'}, 'granularity': 'daily'},
       {'metrics': ['active_devices', 'active_last_30_days', 'sessions'], 'meta': {}, 'order_by': ['date', 'asc'],
        'dimensions': [],
        'filters': {'device_code': ['iPhone', 'iPad', 'iPod', 'AppleTV'], 'user_product_ids': [6900268],
                    'start_date': '2020-03-20', 'end_date': '2020-04-18'}, 'granularity': 'daily'}]
# queries = [{'order_by': ['date', 'asc'], 'dimensions': ['country'],
#                  'metrics': ['active_devices', 'active_last_30_days', 'sessions'], 'meta': {},
#                  'filters': {'country': [u'CN', u'US'], 'user_product_ids': [23696], 'start_date': '2020-03-16',
#                               'end_date': '2020-04-15'}, 'granularity': 'daily'}]
post_data = [dict(query=query) for query in queries]
payload = json.dumps(post_data)

headers = {
    'Authorization': 'Basic Og==',
    'X-SOA-Client-Id': 'aa_conn_iaa_service',
    'AA-Request-ID': '49cd18de82ed4abf83b20d75169c3d33',
    'AA-Sequence-ID': '100011',
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)
print(response.content)
