from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=50)
    desc=models.TextField()
    def _str_(self):
            return self.email

