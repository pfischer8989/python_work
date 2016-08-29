class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

# balls = "You get your balls to the walls man!"

rockofages = Song(["Rise up gather round", "Rock this place to the ground", "Burn it up and go fro broke", "Whatch the night go up in smoke"])

rocku = Song(["Give me an R", "Give me an O", "Give me an C", "Give me a K"])

rockofages.sing_me_a_song()

rocku.sing_me_a_song()

ballstothewalls = Song(["Too many people in this word", "whats your name?", "God bess ya"])

ballstothewalls.sing_me_a_song()


