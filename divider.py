 

def divide(a):
   try:
     x = 10 / int(a)
     print (x)
   except ValueError:
   	 print ("Your input must be an integer")
   except ZeroDivisionError:
     print ("You input must not be zero (0)")


print ("Dividing 10 by an integer")

while True:
   val = input("Provide an integer: ")
   divide (val)

