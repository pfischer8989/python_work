__author__ = 'pfischer'

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide")

if buses > cars:
    print("That is too many buses")
elif buses < cars:
    print("Maybe we could take the buses")
else:
    print("we still can't decide")

if people > buses:
    print("Alright lets just take the buses")
else:
    print("Fine lets stay home")

