from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    desc =models.TextField(max_length=122)
    date =models.DateField()
    #for returning in database with name not like contact object 1
    def __str__(self):
        return self.name