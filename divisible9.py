my_list = [9, 18, 27, 36, 62, 78, 85]

# use anonymous function to filter
result = list(filter(lambda x: (x % 9 == 0), my_list))

# display the result
print("Numbers divisible by 9 are:",result)
