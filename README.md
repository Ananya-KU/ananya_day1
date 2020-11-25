# ananya_day1
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

#Day2

a=20
b=20
c=20
print(a/10)
print(b*50)
print(c+60)
#output
2.0
100
80

str = "world"
print (str.replace("r", "g"))
#output
wogld

a = 120
b = 390.8
print(float(a))
print(int(b))
#output
120.0
390
#Task2 completed
#Thank you

#Day 3
#initializing the dictionaries
fruits = {"grapes": 2, "orange" : 3, "mango": 5}
vegetables = {"onion": 3, "tomato": 4, "potato": 6}
#updating the fruits dictionary
fruits.update(vegetables)
#printing the fruits dictionary
#it contains both the key: value pairs
print(fruits)
{'grapes': 2, 'orange': 3, 'mango': 5, 'onion': 3, 'tomato': 4, 'potato': 6}


myDict = {'a':10,'b':20,'c':30,'d':40}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'b': 20, 'c': 30, 'd': 40}

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

#Creating a set
seta = set([5, 10, 3, 15, 2, 20])
#To find the length use len()
print(len(seta))
6

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print(sn1)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)
Original sets:
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8}
Remove the intersection of a 2nd set from the 1st set using difference_update():
{1, 2, 3}
Remove the intersection of a 2nd set from the 1st set using -= operator:
{1, 2, 3}
