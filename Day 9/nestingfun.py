# 
rental_price=int(input("Price of car per day: "))
days=int(input("Number of days to rent: "))
total=rental_price*days
print("Total car price: ",total)

# 
package_1=int(input("Enter the weight for the first package: ")) 
package_2=int(input("Enter the weight for the second packag: "))
package_3=int(input("Enter the weight for the third packag: "))
total_pack= (package_1+package_2+package_3)*0.8
print("shipment total",total_pack)

# create an expense tracker?
# collect the income from the user
# Collect expense for food,rent,other income from the user
# Get the total amount left aftet expense
# print of remaining total

income=int(input("Enter the Income: "))
food_expense=int(input("Enter the food expense:  "))
rent_expense=int(input("Rent: "))
other_expense=int(input("other expenses: "))
total_expense=food_expense+rent_expense+other_expense
left_amount=income-total_expense
print("Total amount left : ",left_amount)

# create an over-time tracker 
# collec a user monthly pay
# collect the users extra hours worked
# Their bonusis 20% of their monthly salary *extra hours worked 
# print off their overtime bonus pay

monthly_pay=int(input("Monthly pay: "))
extra_hours= int(input("extra hours worked: "))
bonus=0.2*monthly_pay+extra_hours
print("Overtime bonus pay: ",bonus)



