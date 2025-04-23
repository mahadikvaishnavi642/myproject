l1=[1,2,3,4,5]
l2=[3,7,8]
u1=[]#union empty
I1=[]#intersection empty
for i in l1:
    if i not in u1:
        u1.append(i)
for j in l2:
    if j not in u1:
        u1.append(j)
        print("union of two lists",u1)
for i in l1:
    if i in l2:
        I1.append(i)
        print("intersection of two lists",I1)  
