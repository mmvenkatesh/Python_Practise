class c1(object):
    def __init__(self,a,b):
        print self
        self.a=a
        self.b=b
    
    def create(self):
        print 'The insert details {0} {1}'.format(self.a,self.b)

d=c1(10,20)     

class c2(c1):
    def __init__(self,a,b):
        super(c2,self).__init__(a,b)

    def insert(self):
        self.create()


a=c2(10,20) 

           



