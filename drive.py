a=input('enter the first number')
b=input('enter the secound number')
c=input('enter the third number')
d=[]
d.append(a)
d.append(b)
d.append(c)
print('the numbers are',d)
for i in range (0,3):
    for j in range (0,3):
        for k in range (0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i], d[j])
                print(d[i],d[j],d[k])

               