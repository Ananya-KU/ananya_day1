#Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
# list of numbers
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

def filterEvenNum(in_num):

    if(in_num % 2) == 1:
        return True
    else:
        return False

# Demonstrating filter() to remove even numbers
out_filter = filter(filterEvenNum, numbers)

print("Type of filter object: ", type(out_filter))
print("Filtered seq. is as follows: ", list(out_filter))