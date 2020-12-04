import logging

logger = logging.getLogger(__name__)


def a():
    return 1 / 0


# def b():
#     return int("hello")
#
#
# try:
#     a()
#     b()
# except Exception as e:
#     print("hello world")
#     raise e
#

try:
    a()
except Exception as e:
    logger.error("hello",exc_info=True)

