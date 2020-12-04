class aaa:
    def p(self):
        return {"sada":2323}


class bbb(aaa):
    def p(self):
        return super(bbb,self).p()

a=bbb()
print(a.p())