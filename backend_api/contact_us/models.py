from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    emailaddress = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.emailaddress}"
