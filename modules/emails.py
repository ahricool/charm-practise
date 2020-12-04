# from django.core.mail import EmailMultiAlternatives
# from django.conf import settings
# settings.configure()
#
# message = EmailMultiAlternatives("hello", "wwoo", "huaszhang@qq.com", ["huazhang@company.com"], )
# message.attach_alternative("<h1>hello</h1>", "text/html")
# message.send()
#
# ss={(1,2),(3,4),(5,6)}
# for z in zip(*ss)[0]:
#     print(z)
#

s1=[{"a":14,"b":14}]
s2=[{"a":14,"b":15}]
print(s1+s2)
print({ e.get("a"):e.get("b") for e in s1+s2})