from django.db import models

# Create your models here.
class Destination(models.Model):
	title = models.CharField(max_length=100)
	img = models.ImageField(upload_to = 'pics')
	price = models.IntegerField()
	