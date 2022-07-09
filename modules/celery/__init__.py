#
# from collections import OrderedDict
#
# a=OrderedDict()
#
# a.update({1:2})
# a.update({3:4})
# a.update({6:4})
# print(a)
# a.move_to_end()
# print(a.popitem(last=False))
# print(a)

def zsort(s,k):
    slice_len=2*k-2
    for i in range(len(s),slice_len):
        print(i)


print(zsort("todayisaworkday",4))
