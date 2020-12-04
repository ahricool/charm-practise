from wtforms import Form, StringField, validators
from flask import Flask
app=\
    Flask(__name__)

from datetime import datetime
d=datetime(2020,10,10,20,20,20)
d.timestamp()


class StrFields(StringField):
    def process(self, args,**kwargs):
        super(StrFields,self).process(args,**kwargs)


        print("this values"+str(self.data))



from flask.views import View
class TestView(View):
    def dispatch_request(self,*args,**kwargs):
        print("------------params-----------")
        print(args,kwargs)
        from flask import request
        print("------------headers-----------")
        print(type(request.headers))
        print(request.headers)
        print("------------values-----------")
        print(request.values)
        print(request.args)
        # import ipdb;ipdb.set_trace()
        print("------------cookies-----------")
        print(request.cookies)

        print(request.args.to_dict())


        class UsernameForm(Form):
            username = StrFields()

        uf=UsernameForm(request.args)
        print("------------username-----------")
        print("this data "+str(uf.username.data))
        return "Hello"

app.add_url_rule("/",view_func=TestView.as_view("test"))

@app.route("/hello")
def hello():
    print("------------cookies-----------")
    from flask import request
    print(request.cookies)
    return "Hello world"

if __name__=="__main__":
    app.run("127.0.0.1",port=5001,debug=True)