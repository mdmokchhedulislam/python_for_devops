
class test:
    def __init__(self, name, email):
        self.name=name
        self.email=email
    
    def showData(self):
        print("show email", self.email)
    
   

test1 = test("gopal", "gopal@gmail.com")
test1.showData();



class service:
    def start(self):
        print("service is started")


class webservice(service):
     def start(self):
        print("service is started from webservice")



service1=webservice()
service1.start()
