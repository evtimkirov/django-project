from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)