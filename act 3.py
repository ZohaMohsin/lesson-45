class parrot():
    #class variable
    species="bird"
    
    
    def __init__(self,name,age):
    #instance variables
     self.name=name
     self.age=age

p1=parrot("blu",10)
print(" i am a ",p1.species)
print(" my name is {} and i am {} years old".format(p1.name,p1.age))

p2=parrot("rio",12)
print(" i am a ",p2.species)
print("my name is {} and i am {} years old".format(p2.name,p2.age))