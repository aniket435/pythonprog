lower=input('enter the lower limit of interval ')
upper=input('enter the upper limit of interval ')
for num in range(lower,upper +1):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
           else:
               print(num)