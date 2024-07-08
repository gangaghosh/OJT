# Single inheritance 
# When a derived class inherits only from syntax, the base class is called single inheritance. If it has one base class and one derived class it is called single inheritance. 

# Syntax
# class A: #parent class
#  #some code
# class b(A): #child class
#  #some code


# Example
class father: # parent class
    
  def father_name(self):
    print("my father name is selvaraj")
     
class son(father): # child class
  pass

obj_father= father() #object for father class.
obj_son=son() # object for son class.

obj_son.father_name() # you access son class to father class.


