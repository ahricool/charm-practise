

class hello:
    # def __call__(self):
    #     print("hello")

    def hi(self):
        print("hi")

def func():
    print("func")

if __name__=="__main__":

   print(hasattr(hello,"__call__"),
    hasattr(hello(),"__call__"))

   print(hasattr(func, "__call__"),
         hasattr(func(), "__call__"))

   print(hasattr(hello, "hi"),
         hasattr(hello(), "hi"))

   # print("" / "swagger_file")

   SQL = """
   DELETE FROM {0} WHERE id IN (SELECT id FROM {0}
   WHERE create_date< now() - interval '{1} days' LIMIT 10000);
   """.format(1,2)
   print(SQL)


