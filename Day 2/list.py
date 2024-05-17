# 1. Remove an element from a list by value.
my_list = [1, 2, 3, 4, 5, 3]
my_list.remove(4)
print("Removed list:", my_list)


# 2. Create a list and access its elements
vlist = [1, 2, 3, 4, 5]
print("First element:", vlist[0])
print("Last element:", vlist[-1])


# 3. Append an element to a list.
alist = [1, 2, 3]
alist.append(4)
print("Updated list:", alist)


# 4. Find the index of an element in a list
flist = ['a', 'b', 'c', 'd', 'e']
element_to_find = 'c'
index = flist.index(element_to_find)
print(f"Index of {element_to_find}:", index)
