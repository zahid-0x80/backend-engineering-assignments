input_list1 = [1, 6, 6, 2, 7]
input_list2 = input_list1.copy() # Shallow Copy: creates new object

input_list2.append(8)
print(input_list1)
print(input_list2)

#checcking whether they share same reference or not:
# print(f"{input_list1} is {input_list2}")
# print(input_list1 is input_list2)
print(id(input_list1) == id(input_list2))
print(id(input_list1))
print(id(input_list2))

