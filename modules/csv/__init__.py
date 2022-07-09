import csv
import datetime

# with open("/Users/huazhang/workspace/company/aa/tests/ci/unit/analytics/tasks/testdata/everyplay/data/monetization_data_with_rare_country_codes.csv") as r:
#    # with open("/Users/huazhang/Documents/UnityAds")
#     reader=csv.reader(r)
#     count=0
#     for row in reader:
#         count+=1
#         if count<2:
#             continue
#         new_row=[0]*9
#         d=datetime.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S")
#         new_row[0]=d.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#         new_row[1:4]=row[1:4]
#         new_row[4:6]=row[5:7]
#         new_row[6]=row[10]
#         new_row[7:9]=row[8:10]
#         print(",".join(new_row))

# with open(
#         "/Users/huazhang/workspace/company/aa/tests/ci/unit/analytics/tasks/testdata/everyplay/data/monetization_data_with_rare_country_codes.csv") as r:
#     # with open("/Users/huazhang/Documents/UnityAds")
#     reader = csv.reader(r)
#     count = 0
#     for row in reader:
#         count += 1
#         if count < 2:
#             continue
#         new_row = [0] * 9
#         d = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
#         new_row[0] = d.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#         new_row[1:4] = row[1:4]
#         new_row[4:6] = row[5:7]
#         new_row[6] = row[10]
#         new_row[7:9] = row[8:10]
#         print(",".join(new_row))

a = {"login-options": {"api_key": "d22f0a04a9ec24b2f0f59128ae356509a68c3ff144f9a256c707c52a6665e2d2",
                       "organization_id":"5d331dd8933e5c001cf1a77f",
                       "organization_core_id":"284801"},
     "latest-date": "2020-04-10", "num-days": 3}
import json
print(json.dumps(a))


