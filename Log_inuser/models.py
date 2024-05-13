from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    sub_genre = models.CharField(max_length=20, blank=True, null=True)
    image = models.TextField()
    page = models.CharField(max_length=20, blank=True, null=True)
    publish = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "books"
