__author__ = 'pfischer'

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There is a giaint bear here eating cheese. what do you do?")
    print("1. Take the cheese")
    print("2. scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. good job")
    elif bear == "2":
        print("the bear eats your legs off. good job")
    else:
        print("well doing %s is probably better. The bear runs away" % bear)

elif door == "2":
    print("You stare into the endless abyss at cthulhus rentina")
    print("1. Blueberries")
    print("2.Yellow jacket clothespins")
    print("3. Understadning revolvers yelling melodies")

    insantity = input("> ")

    if insantity == "1" or insantity == "2":
        print("Your body survives powered by a mind of jello, good job")
    else:
        print("the insanity rots your eyes into a pool of muck. good job")

else:
    print("you stumble around and fall on a knife and die. good job")