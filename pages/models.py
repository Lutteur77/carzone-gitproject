from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    fb_link = models.URLField(max_length=100)
    tw_link = models.URLField(max_length=100)
    gle_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return self.first_name