## Create a class Book with members as bid,bname,price and author.Add folllowing methods : a.constructor  b.destructor  c.showbook

class Book:
    def __init__(self,id,name,price,author):
        self.bid= id
        self.bname=name
        self.price=price
        self.author=author
        print("Constructor called.")
        
    def __del__(self):
        print("Destructor is called")
        
    def showbook(self):
        print("id:",self.bid)
        print("name:",self.bname)
        print("price:",self.price)
        print("size:",self.author)
        
b1=Book(101,'c',500,'Ajay mithal')
b1.showbook()
del b1
b2=Book(102,"python",1000,"Santosh")
b2.showbook()


