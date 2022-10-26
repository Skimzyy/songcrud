from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length = 50)
    date_released = models.DateTimeField(auto_now_add = False)
    likes = models.IntegerField(default = 0)
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class lyrics(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.content



