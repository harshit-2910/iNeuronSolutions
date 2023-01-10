                                                          # iNeuron Programming Assignment 5 #

#######################################################################################################################################
# 1. Write a Python Program to Find LCM

'''

num1 = int(input('Enter any number: '))
num2 = int(input('Enter any number: '))
bignum=max(num1,num2)
while True:
    if(bignum%num1==0) and (bignum%num2==0):
        break
    else:
        bignum+=1
print(f'LCM is {bignum}')

'''

#######################################################################################################################################
# 2. Write a Python Program to Find HCF

'''

num1 = int(input('Enter any number: '))
num2 = int(input('Enter any number: '))
smallnum=min(num1,num2)
while True:
    if(num1%smallnum==0) and (num2%smallnum==0):
        break
    else:
        smallnum-=1
print(f'HCF is {smallnum}')

'''

#######################################################################################################################################
# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

'''
n = int(input('Enter any number: '))

print(bin(n), "in binary.")
print(oct(n), "in octal.")
print(hex(n), "in hexadecimal.")

'''

#######################################################################################################################################
# 4. Write a Python Program To Find ASCII value of a character

'''

a= input('Enter any character: ')
print(ord(a))

'''

#######################################################################################################################################
# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

'''

x= int(input('enter a number: '))
operation = input('Enter any operation: ')
y= int(input('enter a number: '))

if operation == '+':
    print(x+y)
elif operation == '-':
    print(x-y)
elif operation == '*':
    print(x*y)
elif operation == '/':
    print(x/y)
else:
    print('wrong operator input as asked only enter the basic 4 operator')

'''

##########################################################################################################################################################################################