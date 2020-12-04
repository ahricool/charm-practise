import requests
import json

url = "https://reporting.fyber.com/auth/v1/token"
body = """
{
    "grant_type": "client_credentials",
    "client_id": "4681ba548d49eed3d15e88d48cede369",
    "client_secret": "UNUz5QTDFUGYKIXBjIE4QQxFrOsW917Z-rifvh7oVx6Ny0WVKvZz8Wqy2Zs_PeCV-Crx9dyW8-53346lfTl00GWe3H2Thq6MmIHrzoquO79HX5n8PYTiBY_yDFD7AEVmOmxdjTdWLYroIwmlZq4_Ht6EMrpStDW94H2HfLHNayevwhgH88fuiKmJVaJmEltMJszxDEPh74grKS7xquaj1vRb0eaholIz1zUTczU-grK7bmGwLWyP8zrq5YN3AoDB7OkwCQR-sWPwyYt0mF401nIuIHDbDu3ciNPZSMiNA_vdb894mVxbwVOHmtzQzchs0dyh58dP5132XqIFhoWp2g"
}
"""

requests.post()

# iaa 的 tests/unit/universal_dashboard/device_code_and_date_breakdown/test_device_code_and_date_breakdown.py
a = [{'query': {'dimensions': ['date', 'device_code'],
                'filters': {'user_product_ids': [200, 100], 'country': ['CN', 'US'], 'start_date': '2018-12-13',
                            'end_date': '2018-12-14'},
                'metrics': ['app_store_views:fact_store_page_view', 'paying_users:fact_paying_user',
                            'sessions:fact_iaa_session', 'active_devices:_fact_iaa_active_device',
                            'active_last_30_days:_fact_iaa_30d_active_device'],
                'order_by': ['fact_iaa_session', 'desc', 'date', 'desc', 'device_code', 'desc',
                             'fact_ratio_paying_user_to_active_device', 'desc', 'fact_store_page_view', 'desc',
                             'fact_iaa_ratio_active_device_per_30d_active_device', 'desc',
                             'fact_ratio_download_to_store_page_view', 'desc', 'fact_avg_paying_user', 'desc',
                             'fact_iaa_avg_session_per_active_device', 'desc', 'fact_iaa_avg_30d_active_device', 'desc',
                             'fact_paying_user', 'desc', 'fact_iaa_avg_active_device', 'desc'], 'granularity': 'daily',
                'meta': {'aggregation_mapping': {3: [100]}}}}]

c = [{'query': {'dimensions': ['date', 'country'],
                'filters': {'user_product_ids': [100], 'country': ['US', 'CN'], 'start_date': '2018-12-13',
                            'end_date': '2018-12-14'},
                'metrics': ['active_devices:_fact_iaa_active_device', 'active_last_30_days:_fact_iaa_30d_active_device',
                            'sessions:fact_iaa_session', 'paying_users:fact_paying_user',
                            'app_store_views:fact_store_page_view'],
                'order_by': ['fact_iaa_session', 'desc', 'date', 'desc', 'country_code', 'desc', 'fact_store_page_view',
                             'desc', 'fact_ratio_download_to_store_page_view', 'desc',
                             'fact_ratio_paying_user_to_active_device', 'desc', 'fact_iaa_avg_30d_active_device',
                             'desc', 'fact_avg_paying_user', 'desc', 'fact_paying_user', 'desc',
                             'fact_iaa_avg_session_per_active_device', 'desc',
                             'fact_iaa_ratio_active_device_per_30d_active_device', 'desc', 'fact_iaa_avg_active_device',
                             'desc'], 'granularity': 'daily'}},
     {'query': {'dimensions': ['date'],
                'filters': {'user_product_ids': [100],
                            'start_date': '2018-12-13',
                            'end_date': '2018-12-14'},
                'metrics': [
                    'active_devices:_fact_iaa_active_device',
                    'active_last_30_days:_fact_iaa_30d_active_device',
                    'sessions:fact_iaa_session',
                    'paying_users:fact_paying_user',
                    'app_store_views:fact_store_page_view'],
                'order_by': ['fact_iaa_session', 'desc',
                             'date', 'desc',
                             'fact_store_page_view', 'desc',
                             'fact_ratio_download_to_store_page_view',
                             'desc',
                             'fact_ratio_paying_user_to_active_device',
                             'desc',
                             'fact_iaa_avg_30d_active_device',
                             'desc', 'fact_avg_paying_user',
                             'desc', 'fact_paying_user',
                             'desc',
                             'fact_iaa_avg_session_per_active_device',
                             'desc',
                             'fact_iaa_ratio_active_device_per_30d_active_device',
                             'desc',
                             'fact_iaa_avg_active_device',
                             'desc'],
                'granularity': 'daily'}}]

b = [{'query': {'filters': {'user_product_ids': [1, 2, 3], 'start_date': '2018-11-10', 'end_date': '2018-11-12'},
                'metrics': ['paying_users:fact_paying_user'],
                'granularity': 'daily'}}]

d = [{'active_devices': 15, 'date': '2016-06-10', 'device': 'AppleTV'},
     {'device': 'AppleTV', 'active_devices': 15, 'date': '2016-06-11'},
     {'active_devices': 15, 'device': 'AppleTV', 'date': '2016-06-12'},
     {'active_devices': 15, 'date': '2016-06-13', 'device': 'AppleTV'},
     {'device': 'AppleTV', 'active_devices': 15, 'date': '2016-06-14'},
     {'device': 'AppleTV', 'active_devices': 15, 'date': '2016-06-15'},
     {'date': '2016-06-16', 'device': 'AppleTV', 'active_devices': 15},
     {'active_devices': 15, 'date': '2016-06-17', 'device': 'AppleTV'},
     {'active_devices': 15, 'date': '2016-06-10', 'device': 'iPad'},
     {'active_devices': 15, 'date': '2016-06-11', 'device': 'iPad'},
     {'active_devices': 15, 'date': '2016-06-12', 'device': 'iPad'},
     {'device': 'iPad', 'active_devices': 15, 'date': '2016-06-13'},
     {'date': '2016-06-14', 'device': 'iPad', 'active_devices': 15},
     {'active_devices': 15, 'date': '2016-06-15', 'device': 'iPad'},
     {'active_devices': 15, 'date': '2016-06-16', 'device': 'iPad'},
     {'active_devices': 15, 'date': '2016-06-17', 'device': 'iPad'},
     {'date': '2016-06-10', 'device': 'iPhone', 'active_devices': 15},
     {'active_devices': 15, 'date': '2016-06-11', 'device': 'iPhone'},
     {'active_devices': 15, 'date': '2016-06-12', 'device': 'iPhone'},
     {'active_devices': 15, 'date': '2016-06-13', 'device': 'iPhone'},
     {'device': 'iPhone', 'active_devices': 15, 'date': '2016-06-14'},
     {'active_devices': 15, 'date': '2016-06-15', 'device': 'iPhone'},
     {'active_devices': 15, 'date': '2016-06-16', 'device': 'iPhone'},
     {'active_devices': 15, 'date': '2016-06-17', 'device': 'iPhone'},
     {'active_devices': 15, 'device': 'iPod', 'date': '2016-06-10'},
     {'active_devices': 15, 'device': 'iPod', 'date': '2016-06-11'},
     {'active_devices': 15, 'date': '2016-06-12', 'device': 'iPod'},
     {'date': '2016-06-13', 'device': 'iPod', 'active_devices': 15},
     {'active_devices': 15, 'date': '2016-06-14', 'device': 'iPod'},
     {'device': 'iPod', 'date': '2016-06-15', 'active_devices': 15},
     {'active_devices': 15, 'date': '2016-06-16', 'device': 'iPod'},
     {'date': '2016-06-17', 'device': 'iPod', 'active_devices': 15}]

f = [{u'active_devices': 30, u'date': u'2016-06-10', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-11', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-12', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-13', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-14', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-15', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-16', u'device_code': 148},
     {u'active_devices': 30, u'date': u'2016-06-17', u'device_code': 148}]

g = {'metrics': [{'name': u'active_devices'}], 'dimensions': [{'name': 'date'}, {'name': u'device'}],
     'filters': [{'values': ['product'], 'name': 'asset'}, {'values': [149], 'name': 'user_product_id'},
                 {'start': '2016-06-10', 'end': '2016-06-17', 'name': 'date'}]}

f = [{'query': {'dimensions': ['device_code'],
                'filters': {'user_product_ids': [1, 2, 3], 'start_date': '2018-11-10', 'end_date': '2018-11-12'},
                'metrics': ['paying_users:fact_paying_user'],
                'order_by': ['fact_paying_user', 'desc', 'device_code', 'desc'], 'granularity': 'daily', 'offset': 0,
                'limit': 5, 'meta': {'aggregation_mapping': {3: [1, 2, 3]}}}}]

{'data': [[{'device_code': 3, 'fact_paying_user': 600}]], 'debug_info': '', 'errors': None}
