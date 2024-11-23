class parrot:
    #class variable
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return "{0} sings song {1}" .format(self.name,song)
    
    def dance(self):
         return "{0} is dancing ".format(self.name)
    
p1=parrot("blu",10)
print(p1.sing("'happy'"))
print(p1.dance())
