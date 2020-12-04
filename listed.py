#First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
task_list=["app", "ball", "cat", "dot"]
range_list=[1,2,3,4,5,6,7,8]
converted_list=list(zip(range_list,task_list))
print(converted_list)
