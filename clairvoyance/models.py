from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Pic(models.Model):
	picture = models.ImageField(upload_to='uploads')
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	user = models.ManyToManyField(User)

	def __str__(self):
		return self.id