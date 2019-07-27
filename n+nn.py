n=input('enter the  numbers')
num1=('%s'% n)
num2=('%s%s' %(n,n))
num3=('%s%s%s' %(n,n,n))
print('value of n is',num1)
print('nn form of number is',num2)
print('nnn form of number is',num3)
def add():
    a=num1+num2+num3
    print(a)
print(add())