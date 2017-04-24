from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=15)
	email = models.CharField(max_length=50)
	created = timezone.now()

	def __str__(self):
		return self.id_ + " " + self.username + " " +  self.email + " " + self.created

