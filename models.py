from django.db import models


# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


    def str(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


    def __str__(self):
        return f"{self.artist.first_name} {self.artist.last_name}"


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
       return self.tag_name

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
       return self.category_name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
       return self.title