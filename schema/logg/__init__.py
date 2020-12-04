print("__init__")
print(__name__)

import logging

logger = logging.getLogger(__name__)
# handler = logging.FileHandler("/tmp/log.txt")
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)


def init1():
    logger.error("init1 out put")
