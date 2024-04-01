class calculator():
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def __add__ (self,other):
        print('self.x',self.x,'other.x', other.x, 'self.y' , self.y, 'other.y' ,other.y)
        print(self.x + other.x, ',', self.y+other.y)
    
    def __rsub__(self, other):
        return (self.x-other.x, "," ,self.y-other.y)
 
    def __sub__(self, other):
        return self.x - other.x, ",",  self.y - other.y
if __name__=='__main__':
 c1=calculator(2,3)
 c2=calculator(4,5)
 c3=c1-c2