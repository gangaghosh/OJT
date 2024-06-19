# Fraction 
# In Python, you can also create a type that can hold fractional numbers, like 1/2, 3/5, and so on. To create a Fractional type of number you must import the "fractions" module. Then you need to create a Fraction object.

import fractions as fp
x=fp.Fraction(1,3)
print(x)

# we can also operate fractional numbers. 
# Example
x=fp.Fraction(1,5)
y=fp.Fraction(2,5)
print("%s + %s = %s"%(x,y,(x+y)))

# Fraction objects are automatically reduced to fractions
# Example
x=fp.Fraction(6,12)
print(x)
# Note: You cannot create a fraction with a zero denominator like 5/0 or 0/0