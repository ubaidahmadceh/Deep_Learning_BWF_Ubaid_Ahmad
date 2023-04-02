# creating a tuple (it is immutable and list is mutable) 
fruit_tuple = ("mangoes", "oranges", "apples")
print(fruit_tuple)
print(fruit_tuple[0])
print(fruit_tuple[1])
print(fruit_tuple[2])
print("---------------------")

# using tuple() to create a tuple
fruit_tuple_new = tuple(["mangoes", "oranges", "apples"])
print(fruit_tuple_new)
print("---------------------")

# it doesn't support append
# fruit_tuple_new.append("gauva")
# print(fruit_list_new)
# print("---------------------")

# it doesn't support remove
# fruit_tuple_new.remove("apples")
# print(fruit_tuple_new)
# print("---------------------")