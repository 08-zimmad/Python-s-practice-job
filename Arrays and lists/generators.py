def gen():
    for i in range(0,1000):
        yield(i) 
res = gen()
for i in range(0,1000):
 print(next(res))



# Dict iterator
dc={1:11, 2:22}
dc1=iter(dc.values())
print(type(dc1))
print(next(dc1))
print(next(dc1))

# square using Iterator
class square:
    def __init__(self,length):
        self.length=length
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >=self.length:
            raise StopIteration
        self.current+=1
        return self.current** 2
 
square1=square(5)
print("custom Iterator: ",next(square1))
print("custom Iterator: ",next(square1))
print("custom Iterator: ",next(square1))
print("custom Iterator: ",next(square1))
print("custom Iterator: ",next(square1))
print("custom Iterator: ",next(square1))



# Generator comprehension
sq=(x*x for x in range(9))
print(type(sq))
for q in sq:
    print("square using generator comprehension: ",q)
