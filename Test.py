from datetime import datetime
import json


def func(*args, **kwargs):
    print(args)
    print(kwargs)

    start_time, end_time = sorted([datetime.strptime(args[0], "%Y-%m-%d"), datetime.strptime(args[1], "%Y-%m-%d")])
    print(start_time, end_time)
    start_time, end_time = start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")
    print(start_time, end_time)


def func0(a, b, c):
    print(a, b, c)


if __name__ == "__main__":
    func("2020-9-10", "2019-9-10")

    js = [{
        "salesforce_id": 123,
        "eamil": "1@company.com",
        "activate": True
        },
        {
            "salesforce_id": 234,
            "eamil": "2@company.com",
            "activate": True
        },
        {
            "salesforce_id": 345,
            "eamil": "3@company.com",
            "activate": True
        },
        {
            "salesforce_id": 456,
            "eamil": "4@company.com",
            "activate": True
        },
        {
            "salesforce_id": 567,
            "eamil": "5@company.com",
            "activate": True
        }

    ]

    s = json.dumps(js)

    print(s)
