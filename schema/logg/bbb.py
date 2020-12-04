from schema.logg import init1
from schema.logg.aaa import aaa1
from schema.logg.ccc import ccc1

print("BBB")
print(__name__)



import logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler("/tmp/log23232.txt")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

init1()
aaa1()
ccc1()

logger.error("this is bbb")

#
# # from tempfile import NamedTemporaryFile
# # tmp = NamedTemporaryFile(mode="w")
# # lines_seq =["123","2323"]
# # tmp.writelines(lines_seq)
# # tmp.flush()
# # print(tmp.name)
# # from time import sleep
# # sleep(120)
# #
# s="dsasd%s.{bbb}"%123123
# print(s)
# # s2=s.format(bbb=3333)
# # print(s,s2)
# from  functools import partial
#
# def aa(a,b):
#     print(a,b)
#
#
# func=partial(aa,10)
# # func(20)
# #
# #
# # p="/var/log/company/cmtwewasdasd/asd/sad/sd/i/ascend-provision-sync-{sync_time}.log"
# # import os
# # e=os.path.dirname(p)
# # os.makedirs(e)
#
# import logging
# logging.basicConfig()
# logger = logging.getLogger(__name__)
# logger.error("Hello")
