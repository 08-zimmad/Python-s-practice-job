
class A():
 def __init__ (self,cls):
    self.cls=cls
    print("A instantiated")
 
 def mtd(self,name):
    print('class A mtd and ',name)
 
class B(A):
 def __init__ (self,cls):
    self.cls=cls
    print("B instantiated")
 
 def mtd(self,name):
    print('in B with ', name)
 
if __name__=='__main__':
 a=A('cls')
 b=B('cls')
 
 a.mtd('cls A')
 b.mtd('name B')
