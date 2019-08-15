#different ways of adding rows in the table
from music.models import Album ,Song
Album.objects.all()

a = Album(artist = "Taylor Swift", album_title = "Red",genre = "Country" ,album_logo = "https://upload.wikimedia.org/wikipedia
a.save()

b=Album()
b.artist = "One direction"
b.album_title = "once a day"
b.genre = "punk"
b.album_logo = "http://cdn01.cdn.justjared.com/wp-content/uploads/2014/02/stewart-whoa/kristen-stewart-if-i-do-a-good-scene-i-say-whoa-thats-dope-01.jpg"
b.save()

Album.objects.all()
Album.objects.filter(id =1)
#prints the first one
Album.objects.filter(artist__startswith='Taylor')


#adding songs to database

In [1]: from music.models import Album,Song

In [2]: album1 = Album.objects.get(pk = 1)

In [3]: album1.artist
Out[3]: 'Taylor Swift'

In [4]: song = Song()

In [5]: song.album = album1

In [7]: song.song_title = 'I hate my boyfriend'

In [9]: song.file_type = 'mp3'

In [10]: song.save()


#using create to do all steps in one step

album1.song_set.create(song_title = 'I love bacon' , file_type = 'mp3')
album1.song_set.create(song_title = 'Icecream' , file_type = 'mp3')