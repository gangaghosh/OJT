list_of_airlines=["AL1","AL2","AL3"]
print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])
print("Iterating the list using keyword in")
for airline in list_of_airlines:
    print(airline)

list_of_airlines=["AL1","AL2","AL3"]
airline="AL3"
if airline in list_of_airlines:
    print("Airline found")
else:
    print("Airline not found")

