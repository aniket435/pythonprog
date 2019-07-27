a=input('enter the values of first matrix1')
b=input('enter the values of secound matrix')
x=[]
for i in range(a):
    x.insert(i,[])
    for j in range (b):
        x[i].insert(j, input("enter the value for["+str(i)+"]["+str(j)+"]: "))
        result[j][i]=x[i][j]
for r in result:
    print(r)

        #result[i][j]=a[i][j]+b[i][j]
      # print(result)
