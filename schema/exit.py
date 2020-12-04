# class temp(object):
#     def __init__(self):
#         print("hello world")
#     def __enter__(self):
#         print("asdasd")
#     def __exit__(self, exc_type, exc_value, traceback):
#         print(exc_type, exc_value, traceback)
#         print("wwewew")
#         print("hi")
#         print("we already exc ")
#
# #
# # with temp() as t:
# #     1/0
# #
# # print("end")
#
# a = set(["a", "b", "c"])
# b = set(["a", "e", "f"])
# a |= b
# print(a)
# print(b)
#
# from functools import partial
#
# def func(a, b, c, d=None,e=None,f=None):
#     print("args",a, b, c)
#     print("kwargs",d,e,f)
#
#
# _func=partial(func,1,e=2,f=10,d=9)
#
# _func(e=88)
# #


params = {
    'options': {
        'sessionId': 123,
        'login': "starahri@qq.com",
        'password': "Ahri.goole",
    },
    'settings': {
        'troubleshooting': True,
        'testing': False,
    }
}
import json

print(json.dumps(params))

a = {"num_days": 32,
     "latest_date": "2018-03-11",
     "send_success_import_email": false,
     "workflow_name": "ad_h",
     "historical_scrape": true,
     "meta": {"task_path": "ad_h", "celery_options": {}},
     "ad_network": "apple_search_ads",
     "historical": true,
     "appcare_id": 625845}

b = {"latest_date": "2018-03-11",
     "modes": [["expense"]],
     "send_success_import_email": false,
     "ad_network": "apple_search_ads",
     "workflow_name": "ad_h",
     "task_unique_id": "1590675737_3921738",
     "historical_scrape": true,
     "meta": {"task_path": "ad_h/ads/adss/advana_ntq_scrape", "celery_options": {}},
     "historical": true,
     "appcare_id": 625845, "num_days": 32}

adm = [{'scrape_items': [
    {'latest_date': datetime.date(2020, 6, 1), 'scrape_day': '1', 'workflow_name': 'ad_m', 'scrape_function': None,
     'scrape_hour': '14', 'launch_strategy': None, 'num_days': 31},
    {'latest_date': datetime.date(2020, 6, 1), 'scrape_day': '*', 'scrape_function': None, 'scrape_hour': '14',
     'launch_strategy': None, 'num_days': 7}],
    'skip_scrape_status': [14, 20, 100]}]
params = {"latest_date": "2018-05-11", "modes": [["expense"]], "send_success_import_email": false,
          "ad_network": "apple_search_ads", "workflow_name": "ad_h", "task_unique_id": "1590771350_4660909",
          "historical_scrape": true, "meta": {"task_path": "ad_h/ads/adss/advana_ntq_scrape", "celery_options": {}},
          "historical": true, "appcare_id": 451895, "num_days": 32}


from webanalytics.advana.workflow.tasks import advana_ntq_scrape
args=()
import json
js="""{"latest_date": "2018-05-11", "modes": [["expense"]], "send_success_import_email": false,
          "ad_network": "apple_search_ads", "workflow_name": "ad_h", "task_unique_id": "1590771350_4660909",
          "historical_scrape": true, "meta": {"task_path": "ad_h/ads/adss/advana_ntq_scrape", "celery_options": {}},
          "historical": true, "appcare_id": 451895, "num_days": 32,
          "proxies":["@1.2.3.4"]}"""
json.loads(js)
meta=json.loads(js)
advana_ntq_scrape(*args,**meta)