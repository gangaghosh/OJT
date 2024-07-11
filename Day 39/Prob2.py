# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once

import random

def random_char():
    char_list=['a','e','i','o','u']
    random.shuffle(char_list)    # random.shuffle function in Python is used to randomly shuffle the elements of a list in place
    return ''.join(char_list)
print(random_char())

