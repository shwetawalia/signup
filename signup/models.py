from django.db import models

class projecttable(models.Model):
	username=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	
	def __str__(self):
		return self.username +'==>' + self.email + '==>' + self.password 
