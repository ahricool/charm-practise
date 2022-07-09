# class
#
# class Bird:
#     def __init__(self):
#         self.bird="qiu..qiu.."
#
#
# # class Animal()Animal
#
#
# a=['title', 'author', 'units', 'publisher proceeds', 'currency of proceeds', 'customer price', 'customer currency', 'country code', 'product type identifier', 'pre-order', 'promo code', 'isbn', 'apple identifier', 'vendor identifier', 'vendor offer code', 'begin date', 'end date', 'publisher', 'imprint', 'version', 'category']
#
#
#
#
#
#
#
# category
#
# def set_cursor(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
#
#
# class Query:
#     def __init__(self):
#         self.cursor=None
#
#     @set_cursor
#     def get_cursor(self):
#         print(self.cursor)
#
#

class A:
    def hello(self,str):
        print(str)
class B(A):
    def hello(self):
        super(B,self).hello("IDWOE")
        print("Asda")

B().hello()
