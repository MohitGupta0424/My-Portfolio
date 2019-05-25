from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    pub_date = models.DateField()
    blogText = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images/')
