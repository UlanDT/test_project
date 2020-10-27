from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.TextField()

    def __str__(self):
        return self.full_name
