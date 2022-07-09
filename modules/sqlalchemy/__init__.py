# # from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # # from sqlalchemy import Column, String, Integer
# # #
# # # engine = create_engine('mysql+pymysql://root@localhost:3306/blog')
# # # Base = declarative_base()
# # #
# # #
# # # class User(Base):
# # #     __tablename__ = 'users'
# # #     id = Column(Integer, primary_key=True)
# # #     username = Column(String(64), nullable=False, index=True)
# # #     password = Column(String(64), nullable=False)
# # #     email = Column(String(64), nullable=False, index=True)
# # #
# # #     def __repr__(self):
# # #         return '%s(%r)' % (self.__class__.__name__, self.username)
# #
# #
# # Base.metadata.create_all(engine)
# #
# # aa = {"meta": {"task_path": "submit_marketo_form", "celery_options": {}}, "program_name": "01.2 Registration Form",
# #       "mkt_trk_cookie": "id:756-LMY-597&token:_mch-company.org-1563247823732-30191",
# #       "params": {"offertype__c": "Product Registration", "AALastLoginPostalCode__c": "-", "FirstName": "yang",
# #                  "aaAccountStatus": "Unverified", "utm_term__c": "", "AA_LastVisitState__c": "-", "LastName": "wang",
# #                  "Company": "Fake Customer_1981", "Job_Function__c": "Product", "Company_Size_Survey__c": "",
# #                  "referrer": "", "utm_content__c": "", "Industry_Simplified__c": "", "Unsubscribed": false,
# #                  "utm_campaign__c": "", "sfdcid__c": "", "AA_LastVisitCountry__c": "-", "utm_source__c": "",
# #                  "utm_medium__c": "", "AA_LastVisitCity__c": "-"}, "email": "yangwang+re9@company.com"}
# #
# # aa = {{"date": "2019-07-31", "func_naame": "send_password_reset_email",
# #        "meta": {"task_path": "send_aa_emails", "celery_options": {"queue": "send_aa_emails_instant"}},
# #        "params": "{\"user_id\": 100, \"context\": {\"account\": {\"id\": 1234}, \"base_url\": \"https://django04.stg-feature.company.org\", \"activate_url_with_code\": \"/account/password-reset/2s-2e1uzm-bc38cbd365184b4ad166/\"}}"}}
#
# import argparse
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Automatically detect ITC vendors.')
#     parser.add_argument('-u', '--user')
#     parser.set_defaults(user=None)
#     args = parser.parse_args()
#
#     parser = argparse.ArgumentParser(description='Automatically detect ITC vendors.')
#     parser.add_argument('-u', '--user')
#     parser.set_defaults(user=None)
#     args = parser.parse_args()
#
#     if args.user=="all":
#         print(1)
# #     elif args.user:
# #         print(2)
# #     else:
# # #         print("Please use --user all or --user user_id")
# #
# # s='""," s",None'
# # print(any(map(lambda x:x.strip() if x is not None else None,eval("[%s]"%(s)))))
#
#
#
# from webanalytics.mongodb.utils import get_mongodb_uri
# import pymongo
#
# client = pymongo.MongoClient(host=get_mongodb_uri())
# client[]
#

from functools import partial
from datetime import datetime

# # strptime = partial(datetime.strptime, format='%Y-%m-%dT%H:%M:%S')
# # to = strptime("2020-10-20T20:20:20")
# # print(to)
# def a(aa,bb):
#     print(aa)
#     print(bb)
#
#
# func=partial(a,bb="hello")
# func("wworld")


for k in {"123":"1234",1:2}.pop(1):
    print(k)
    print("heelo")
