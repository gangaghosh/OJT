# Multilevel inheritance 
# Multilevel inheritance is the concept where a subclass inherits properties from multiple base classes. It has one base class and two (or) more derived classes called multilevel inheritance.

# Syntax
#  class A: #parent class
#  #some code
# 
#  class B(A): #child class
#  #some code
# 
#  class C(B): #child class
#     #some code


# Example
class g_father:# parent class
  def g_father_name(self):
    print("my father name is ramasamy")

class father(g_father): # child class
 def father_name(self):
   print("my father name is selvaraj")

class son(father): # child class
  def son_name(self):
    print("my name is surya")

obj_g_father= father() # object for g_father class.

obj_father= father() # object for father class.

obj_son=son() # object for son class.

obj_son.g_father_name() # you access son class to g_father class.

obj_son.father_name() # you access son class to father class.

obj_son.son_name() # you access same class.