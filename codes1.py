output = [(0,31)]
moves = 310*3
radius = 30
x=0
y=11
sign=1
h=False
for y in range(radius,-radius-1,-1):
    for j in range(-radius,radius+1):
        x=sign*j
        print(x, y, moves)
        output.append((x,y))
        #print(x,y)
        moves-=1
        if y - (-radius - 1) >= moves-1:
            h=True
            break
    #else:
    #    print("happening")
    #    h=True
   #     break
    if h:
        break
    sign=-sign
    #print("moves ",moves, y-(-radius-1))
while y-(-radius-1)>1:
    y-=1
    moves-=1
    print(y)
    output.append((x,y))
output.append((0,-31))
print(output)
print(len(output))
print(moves)