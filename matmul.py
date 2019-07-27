a=input('enter the values of first  matrix')
b=input('enter the values of secound matrix')
c=input('enter the values of third matrix')
d=input('enter the values of fourth matrix')
x=[]
for i in range(a):
    x.insert(i,[])
    for j in range (b):
        x[i].insert(j, input("enter the value for["+str(i)+"]["+str(j)+"]: "))
        print(x)
y=[]
for i in range(c):
    y.insert(i,[])
    for j in range (d):
        y[i].insert(j, input("enter the value for["+str(i)+"]["+str(j)+"]: "))
        print(y)
result = [[0,0,0,0],
         [0,0,0,0]]


for i in range(len(x)):

   for j in range(len(y[0])):

       for k in range(len(y)):
           result[i][j] += x[i][k] * y[k][j]

for r in result:
   print"the multipicatio of given matrix is"+str(r)