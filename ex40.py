# This is the fortieth exercise.
# Date: 2014-06-27

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def length(self):
        print len(self.lyrics)

happy_bday = Song(["Happy birthday to you","I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

song_variable = ["First line", "Second line", "Third line"]
song_var = Song(song_variable)
song_var.sing_me_a_song()
song_var.length()

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()