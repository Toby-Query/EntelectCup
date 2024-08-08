dict={}
with open('4.txt') as openfileobject:
    x=0
    for line in openfileobject:
        if (x==0):
            x+=1
            continue
        #print(line)
        line=line[1:-2]
        #print(line)
        dummy = line.split(';')
        #print(dummy)
        if (len(dummy)!=3):
            continue
        dict[eval(dummy[0])]=int(dummy[1])*float(dummy[2])
#print(dict)

output = [(0,11)]
radius = 210
addTuple = (-10,10)
visited = [(0,11)]

def value(tup):
    return dict[tup]

for x in range(-radius, radius+1):
    if(value((x,radius))>value(addTuple)):
        addTuple=(x,radius)
    print(dict[(x,radius)])
output.append(addTuple)
visited.append(addTuple)
print(output)
print(dict[addTuple])
print(addTuple)
for i in range(-radius,radius+1):
    for j in range(-radius,radius+1):
        if (dict[(i,j)]>3):
            print("3", end="")
        elif dict[(i,j)]>2 :
            print("2", end="")
        elif dict[(i,j)]>1 :
            print("1", end="")
        elif dict[(i,j)]>0 :
            print("0", end="")
        else:
            print("-", end="")
    print()