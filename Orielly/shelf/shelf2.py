import shelve

def shelfme(name, score):

	data = shelve.open(r'/Users/pfischer/Documents/python/test/shelf/highscore.shelf')

	if name in data:
		hiscore = max(data[name], score)
		data[name] = hiscore
		# print("This is the new score", data[name])
		data.close()
		return data[name]
		
	else:
		data[name] = score
		# print("This is the score", data[name])
		data.close()
		return data[name]
		
	

if __name__ == "__main__":
   while True:
      name = input("What is your name?: ")
      score = int(input("What is your score?: "))
      shelfme(name, score)