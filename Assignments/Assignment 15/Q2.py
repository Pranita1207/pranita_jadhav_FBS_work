## Create a class product with members as pid,pname,price,quality.Add following methods:  d.Constructor  e.Destructor  f.showProduct

class product:
    def __init__(self,id,name,price,quality):
        self.pid=id
        self.pname= name
        self.price = price
        self.quality= quality
        print("Constructor called")
        
    def __del__(self):
        print("Destructor is called")
        
    def showproduct(self):
        print("id:",self.pid)
        print("name:",self.pname)
        print("price:",self.price)
        print("quality:",self.quality)
        
        
p1=product(101,"milk",20,"good")
p1.showproduct()
del p1
p2=product(102,"cadbuary",40,"good")
p2.showproduct()
        
        