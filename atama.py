#x=5
#y=10
#z=20
x,y,z=5,16,20
print(x,y,z)
x,y=y,x
print(x,y,z)
x+=5
print(x,y,z)
x-=5
print(x,y,z)
#x%=5
#print(x,y,z)
x//=5
print(x,y,z)
y**=z
print(x,y,z)

values=1,2,3,4,5
print(values)
print(type(values))
x,y,*z=values
print(x,y,z[1])