# while loop
i=2
while i < 8:
    print(i)
    i +=1

    # Program to add natural numbers upto
    # add =1+2+3+...+n
    n=20
    add=0
    i=1
    while i <=n:
        add =add +i
        i=i+1
    print("The sum is",add)

    # Break Statement
    a=10
    while a>0:
        a-= 1
        if(a!=5):
            print(a)
        else:
            break
for a in "python":
    if a == "h":
         break
    print(a)
print("Loop ends")
# Continue Statement
a=10
while a>0:
    a-=1
    if(a!=5):
        print(a)
    else:
        continue
    # skip 5 and loop is on iteration

for  a in "python" :
        if a == "h":
            continue
        print(a)

print("Loop ends")

# pass
v1= {'p','a','s','s'}
for v in v1:
    pass
# Example: Printing 1 to 20.
i=1 
while(i<=20):
     print(i) 
     i=i+1

# example 2:printing Table of given number.
num=int(input("Enter a Number:"))
i=1
while(i<=10):
    print(num *i)
    i=i+1

# Example 3: Printing reverse of a number.
num = int(input("Enter a Number : "))
rev = 0 
while(num != 0):
    rem = num % 10
    rev = rev * 10 + rem 
    num = int(num / 10)

print(rev)

# while loop with else
# Example 4: #program to check #weather the given number is #prime number or not
num = int(input("Enter a Number : "))
i=2; 
while(i<num): 
    if(num%i==0):
         print("%d is not a prime number..."%num)
         break
         i=i+1
    else: 
     print("%d is a prime number..."%num)

