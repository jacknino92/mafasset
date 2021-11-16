from django.db import models

class Datas(models.Model):
	Email=models.CharField(max_length=30,default="")
	Password=models.CharField(max_length=20,default="")
