# Write a  Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

def sequence(value):
   if len(value)==len(set(value)):   # set is a built-in data type that represents an unordered collection of unique elements
       return True
   else:
       return False

print(sequence([1,2,3,4,5]))
print(sequence([1,2,3,3,4,]))