import re
def _parse_daily_report_name():
    report_name="1111-22-33_csv.csv"
    compiled_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})_%s.csv" % "csv")
    match = compiled_pattern.search(report_name)
    report_date_index = 1
    if match:
        print(match.group(report_date_index))
    else:
        new_compiled_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d+)_%s.csv" % user_id)
        new_match = new_compiled_pattern.search(report_name)
        if new_match:
            vendor_id_index = 2
            vendor_id_from_report_name = new_match.group(vendor_id_index)
            if vendor_id_str == vendor_id_from_report_name:
                return DAILY, new_match.group(report_date_index)
    return None, None

if __name__=="__main__":
    # import os
    #
    # CSV_STORE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    # print(CSV_STORE_ROOT)
    # CSV_STORE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gp_daily_sales'))
    # print(CSV_STORE_ROOT)
    #
    # ITC_SALES_REPORTS_STORE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sales_reports', 'user'))
    # print(ITC_SALES_REPORTS_STORE_ROOT)
    #
    # import schema
    # ITC_SALES_REPORTS_STORE_ROOT = os.path.abspath(os.path.join(schema.aa, 'sales_reports', 'user'))
    # print(ITC_SALES_REPORTS_STORE_ROOT)
    #
    # import glob, os
    #
    # pattern = "/Users/huazhang/workspace/CharmTest/modules/regex/*"
    #
    # d = glob.glob(pattern)
    # for i in d:
    #     mtime = os.stat(i).st_mtime
    #     print(i, mtime)
    import glob

    pattern = "/Users/huazhang/workspace/CharmTest/modules/regex/2"

    d = set(glob.glob(pattern))
    for i in d:
        mtime = os.stat(i).st_mtime
        print(i, mtime)

# /Users/huazhang/workspace/CharmTest/modules/regex/__init__.py 1571294393.6881585
# /Users/huazhang/workspace/CharmTest/modules/regex/regextest.py 1569208508.9634302
# /Users/huazhang/workspace/CharmTest/modules/regex 1571294393.6881719

# /Users/huazhang/workspace/CharmTest/modules/regex/__init__.py 1571294393.6881585
# /Users/huazhang/workspace/CharmTest/modules/regex/regextest.py 1574063564.3647857
# /Users/huazhang/workspace/CharmTest/modules/regex 1574063564.369178
#
#     import os
#     os.path.abspath()
#
#     import json
#     print(json.dumps({'jsonRequest':json.dumps({
#         "mode": "Robot.XML",
#         "queryInput": "[p=Reporter.properties, Sales.getAccounts]",
#         "salesurl": "https://reportingitc-reporter.apple.com/reportservice/sales/v1",
#         "accesstoken": "a482fa66-1399-4eca-9339-7d1778cf976d",
#         "version": "2.2"
#     })}))

    import re

    base_name="2019-01-023_341.csv"

    z=re.sub("(?<=_)\d+_\d+(?=\.csv$)","123_123",base_name)
    print(z)

    if not "":
        print("sdsf")