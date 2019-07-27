a=input('enter the first number')
b=input('enter the secound number')
c=input('enter the third number')
if (a>b) and (a>c):
    largest = a
elif (b>a) and (b>c):
    largest = b
else:
    largest = c
print('the largest number among '+str(a)+'  ,' +str(b)+ '  and ' +str(c)+' is ',largest)