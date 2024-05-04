
# Dunder method
class dunder:
 def __init__(self,a):
    self.a=a
 def __add__(self,a):
    return a
 
if __name__=='__main__':
 c=dunder(2)
 a=dunder(4)
 
 print(c.__class__.__name__)
 print(c+4)
 print(a.__add__(9))
