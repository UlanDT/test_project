from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=150)
    position = models.TextField()

    def __str__(self):
        return self.full_name
