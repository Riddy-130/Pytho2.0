my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
[unique_list.append(item) for item in my_list if item not in unique_list]
print(unique_list) 
