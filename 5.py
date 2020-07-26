squares=[]
for square in range(1,6):
    square=square**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
##
square2=[value**2 for value in range(1,6)]
players=['charles', 'michael', 'ronaldo', 'john']
print(players[-2:]) #If you use minus, it starts from the end
a=players[:]
print(a)
dimensions=(200,50) #This is an immutable list so you can't change values of this list
print(dimensions)
