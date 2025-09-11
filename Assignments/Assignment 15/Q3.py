## Create a class shirt with members as sid,sname,type,price and size.Add following methods: g.Constructor  h. destructor i.showshirt

class shirt:
    def __init__(self,id,name,type,price,size):
        self.sid= id
        self.sname=name
        self.type=type
        self.price=price
        self.size=size
        print("Constructor created")
        
    def __del__(self):
        print("shirt object is destroyed")
        
    def showshirt(self):
        print("id:",self.sid)
        print("name:",self.sname)
        print("type:",self.type)
        print("price:",self.price)
        print("size:",self.size)
""    
s1=shirt(10,'khadi','formal',500,26)
s1.showshirt()
del s1
s2=shirt(11,'kurta','traditional',1000,28)
s2.showshirt()
