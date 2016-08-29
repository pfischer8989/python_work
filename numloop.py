#!/usr/local/bin/python3

numbers = []

while True:
    try:
       line = input("number: ") 
       
       number = int(line)
       numbers.append(number)
           #return number
    
    except ValueError as err:
           print(err)

print("numbers:", numbers)

for x in numbers:
    print("the number is: ", numbers)
    
    
  