from django.db import models

class parents(models.Model):
	name=models.CharField(max_length=120)
	description=models.TextField(max_length=120)
	def __unicode__(self):
		return self.name
		

# Create your models here.
