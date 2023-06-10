class Myclass:
    x=4
hiClass=Myclass()
# print=(hiClass.x)
print("hello")

class Arithmetics:
    def sum(a,b):
        print(a+b)
    def sub(c,d):
        print(c-d)
    def mul(e,f):
        print(e*f)
    def div(g,h):
        print(g/h)
myArth = Arithmetics

q=int(input('enter a number for q '))
w=int(input('enter a number for w '))
y=int(input('enter a number for y '))
z=int(input('enter a number for z '))

myArth.sum(q,w)
myArth.sub(w,y)
myArth.mul(y,z)
myArth.div(z,q)