from django.db import models

# Create your models here.

class Form(models.Model):
 

     email=models.EmailField()
     phone=models.CharField(max_length=50)

     def __str__(self):
        return self.email
    
