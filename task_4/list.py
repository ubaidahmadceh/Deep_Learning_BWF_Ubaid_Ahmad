# creating a list
fruit_list = ["mangoes", "oranges", "apples"]
print(fruit_list)
print(fruit_list[0])
print(fruit_list[1])
print(fruit_list[2])
print("---------------------")

# using list() to create a list
fruit_list_new = list(["mangoes", "oranges", "apples"])
print(fruit_list_new)
print("---------------------")

# add a new item
fruit_list_new.append("gauva")
print(fruit_list_new)
print("---------------------")

# remove an item
fruit_list_new.remove("gauva")
print(fruit_list_new)
print("---------------------")

# sorting the list
print(sorted(fruit_list_new))
