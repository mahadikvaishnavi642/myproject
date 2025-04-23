#program for union of two list
a = [1,2,3,4,5,6]
b = [2,7,8,9,5]
c = []
for i in a:
    if(a not in c):
        c.append(i)
for j in b:
    if(b not in c):
        c.append(j)
print("Union of two list is = ",c)
        
