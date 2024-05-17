# 1. Iterate over keys and values in a dictionary.
my_dict = {'name:':'Alice','age:': 25,'city:':'New York'}
for i in my_dict:
    print(i,my_dict[i])


# 2. Create a dictionary and access its elements
dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Name:", dict['name'])
print("Age:", dict['age'])
print("City:", dict['city'])


# 3. Add a key-value pair to an existing dictionary.
edict = {'name': 'Alice', 'age': 30}
edict['city'] = 'New York'
print("Updated dictionary:", edict)


# 4. Check if a key exists in a dictionary
kdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key_to_check = 'city'
if key_to_check in kdict:
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")
