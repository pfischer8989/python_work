import shelve


def shelfme(name, score):
  
   #print(score)

   data = shelve.open(r'/Users/pfischer/Documents/python/test/shelf/highscore.shelf')

   data[name] = score

   # print (name)

   #for x in data.items():
   #   print (x)

   #print ("this is the data", data[name])
   chk = data[name]

   key = data.keys()

   print("This is Data name", data[name])
   print("This is chk", chk)
   print("This is the key", key)
   print("pulling %name", dict.get('name'))

   if name in data.items():
      print ("Name in data")
      

      for x in data.items():
         print (x)

      if data[name] > score:
         data[name] = score
         print ("This is the score after the if", score)
         return score
     

      else:
      
      
         return score
   
   else:
      return score     




   data.close()


if __name__ == "__main__":
   while True:
      name = input("What is your name?: ")
      score = int(input("What is your score?: "))
      highscore = shelfme(name, score)
      print (highscore)


