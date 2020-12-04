#Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
def merge(list1, list2): 
      
    merged_list = tuple(zip(list1, list2))  
    return merged_list 
      
list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c'] 
print(merge(list1, list2)) 