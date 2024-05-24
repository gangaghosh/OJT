# Create a class called Person with attributes for name, age, and email. Implement validation to ensure that age is a positive integer and email follows a valid format.    

import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = self.validate_age(age)
        self.email = self.validate_email(email)

    def validate_age(self, age):
        if isinstance(age, int) and age >= 0:
            return age
        else:
            raise ValueError("Age must be a positive integer.")

    def validate_email(self, email):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return email
        else:
            raise ValueError("Invalid email format.")

# Testing data validation in the Person class
try:
    person1 = Person("Alice", 25, "alice@example.com")
    print("Person:", person1.name, person1.age, person1.email)
except ValueError as e:
    print(e)

try:
    person2 = Person("Bob", -30, "bob@example")
    print("Person:", person2.name, person2.age, person2.email)
except ValueError as e:
    print(e)
