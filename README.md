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
