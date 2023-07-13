from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "message from "+ self.name
