import logging
try:
    1/0
except ZeroDivisionError as e:
    logging.error("message")

# ERROR:root:message

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("message")

# ERROR:root:message
# Traceback (most recent call last):
#   File "/Users/huazhang/workspace/CharmTest/modules/sqlalchemy_tutorial/log.py", line 10, in <module>
#     1/0
# ZeroDivisionError: division by zero


try:
    1/0
except ZeroDivisionError as e:
    logging.error("message",exc_info=1)
#
# ERROR:root:message
# Traceback (most recent call last):
#   File "/Users/huazhang/workspace/CharmTest/modules/sqlalchemy_tutorial/log.py", line 22, in <module>
#     1/0
# ZeroDivisionError: division by zero