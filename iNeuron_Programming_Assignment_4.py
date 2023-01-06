                                                   # iNeuron Programming Assignment 4 #

#################################################################################################
# 1. Write a Python Program to Find the Factorial of a Number?

'''
def factorial(x):
    fac = 1
    for i in range(1,x+1):
        fac *=i
    return fac

n= int(input('Please enter a number: '))

print(factorial(n))

'''

#################################################################################################
# 2. Write a Python Program to Display the multiplication Table?

'''
n= int(input('Enter a number: '))
x=10
for i in range (1,x+1):
    print(n ,'*' ,i ,'=' ,(n*i))

'''

#################################################################################################
# 3. Write a Python Program to Print the Fibonacci sequence?

'''
n = int(input('Input an number: '))
a=0
b=1
for i in range (n+1):
    c=a+b
    a=b
    b=c
    print(c)
'''

#################################################################################################
# 4. Write a Python Program to Check Armstrong Number?

'''

n=int(input('Enter a number: '))
sum=0
temp = n
while temp>0:
    a=temp%10
    sum+=a**3
    temp//=10
if n == sum:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')

'''

#################################################################################################

# 5. Write a Python Program to Find Armstrong Number in an Interval?

'''

lower=int(input('Enter Lower Limit : '))
upper=int(input('Enter Upper Limit : '))
if lower >= 1:
    for i in range (lower,upper+1):
        sum=0
        temp = i
        while temp>0:
            a=temp%10
            sum+=a**3
            temp//=10
        if i == sum:
            print(i)
        else:
            pass

'''

#################################################################################################
# 6. Write a Python Program to Find the Sum of Natural Numbers?

'''

n= int(input('Enter any number: '))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

'''

##################################################################################################################################################################################################