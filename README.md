#Best enlist 30 days internship on Python
#ananya_day1
>>>print("Hello World!")
Hello World!
>>>print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> print('30 days 30 hour challenge')
30 days 30 hour challenge
>>>Hours="thirty"
>>> print(Hours)
thirty
>>>Days="Thirty days"
>>> print(Days[0])
T
>>> Challenge="I will win"
>>> print(Challenge[7:10])
win
>>> Challenge="I will win"
>>> print(len(Challenge))
10
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+b
>>> print(c)
30 Days30 hours
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+""+b
>>> print(c)
30 Days30 hours
>>> text="Thirty days and Thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> str="BestEnlist"
>>> print(str[1:])
estEnlist
#Task1 completed
#Thank you

#Day4
def work_insert(work):
    a = int(input("enter no to insert into list"))
    work.append(a)
    print(work)
    return


def work_delete(work):
    a = int(input("enter no to delete in list"))
    work.remove(a)
    print(work)
    return

work =[45,56,78,99,90]
work_insert(work)
work_delete(work)
minimum = min(work)
maximum = max(work)
print(minimum)
print(maximum)
#output 
10
45
enter no to insert into list[45,56,78,99,90,10]
enter no to delete in list[56,78,99,90,10]
10
99

def Reverse(tuples): 
    new_tup = () 
   for k in reversed(tuples): 
        new_tup = new_tup + (k,) 
   print new_tup

tuples = (10, 11, 12, 13, 14, 15) 
Reverse(tuples) 
#Output
(15, 14, 13, 12, 11, 10)

k=(10,20,30,40,50)
y=list(k)
print(type(y))
#output
<class 'list'>
 
#Day 5
def addition(x,y):
    print("addition of two numbers",(x+y))
def subtraction(x,y):
    print("subtraction of two numbers",(x-y))

def multiplication(x,y):
    print("multiplication of two numbers",(x*y))
def division(x,y):
    print("division of two numbers",(x/y))

x= int(input("enter the value of x"))
y= int(input("\nenter the value of y\n"))
addition(x,y)
subtraction(x,y)
division(x,y)
multiplication(x,y)
#Output 
enter value of x
enter value of y
addition of two numbers 30
subtraction of two numbers 10
division of two numbers 2.0
multiplication of two numbers 200


def covid(patient_name,body_temp=98):    
    patient_details={‘patient_name’:name,’body_temp’:body_temperature}
    print(patient_details)
    
patient_name=input(‘enter the patient name\n’)
body_temperature=int(input(‘enter the patient body temperature’))
covid(patient_name, temperature)
#Output
enter the patient name 
Ashish
enter the body temperature98
{'patient_name': 'Ashish','body_temp': 98}
#Task5 completed
#Thank You

#Day 6
list1=[1,3,5,7,9]
for i in list1:
    print(i,i+2)
#Output
1 3
3 5
5 7
7 9
9 11

for i in range(5,0, -1): 
	for j in range(i, 0, -1): 
		print(j, end='') 
	print() 
#Output
54321
4321
321
21
1

nterms = int(input("How many terms you want? "))  
# first two terms  
n1 = 0  
n2 = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while count < nterms:  
       nth = n1 + n2  
       print(nth,end=' , ')  
       # update values  
       n1 = n2  
       n2 = nth  
       count += 1  
#Output
How many terms? 7
Fibonacci sequence:
0
1
1
2
3
5
8

#A positive integer is called an Armstrong number of order n 
num = int(input("Enter a number: "))

#initialize sum
sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

#display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#Output1
Enter a number: 663
663 is not an Armstrong number

#Output 2
Enter a number: 407
407 is an Armstrong number

num = 9
#To take input from the user
#num = int(input("Display multiplication table of? "))
#Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
#output
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
#Output1
Enter a number: 10
Positive number
#Output2
Enter a number:-10
Negative number

print("Enter number of days: ")
days=int(input())
years = (days / 365)
print(years)
#Output
Enter number of days: 
365
1.0

#importing math module
import math
#number 
x = 0.50
#math.cos()
print("math.cos(",x,"): ", math.cos(x));
#math.sin()
print("math.sin(",x,"): ", math.sin(x));
#math.tan()
print("math.tan(",x,"): ", math.tan(x));
#Output
math.cos( 0.5 ):  0.8775825618903728
math.sin( 0.5 ):  0.479425538604203
math.tan( 0.5 ):  0.5463024898437905

print("Calculator:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#input choice
ch=int(input("Enter Choice(1-4): "))
if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
#Output
Calculator:
1.Add
2.Subtract
3.Multiply
4.Divide
Enter Choice(1-4): 4
Enter A: 20
20
Enter B:5
Quotient =  4.0
#Task 6 Completed
#Thank you
