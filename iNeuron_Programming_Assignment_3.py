# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
'''
x=int(input('Please enter a number:'))

if x>0:
    print('positive number')
if x<0:
    print('negative number')
if x == 0:
    print('Zero')

'''
#################################################################################################

# 2. Write a Python Program to Check if a Number is Odd or Even?

'''
x= int(input('Please Enter a number: '))

if x%2==0:
    print('even')
else:
    print('odd')

'''

#################################################################################################

# 3. Write a Python Program to Check Leap Year?

'''
x = int(input('Please enter an Year: '))

if (x%400==0 or x%100!=0 and x%4==0):
    print('Leap year')
else:
    print('Not a Leap Year')

'''

#################################################################################################


# 4. Write a Python Program to Check Prime Number?

'''
x= int(input('Please enter a Number: '))

if x==1:
    print('Neither Prime nor Composite')
for i in range(2, (int(2+x/2)+1)):
    if x%i==0:
        print('not a prime number')
        break
    else:
        print('prime number')
        break

'''

#################################################################################################

'''
n=1
x=10000

for i in range(n, x+1):
    if i>1:
        for j in range (2,i):
            if (i%j) == 0:
                break
        else:
            print(i)
            

'''

#################################################################################################