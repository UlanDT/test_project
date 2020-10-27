from django.db import models

from customers.models import Customer
from employees.models import Employee


class Order(models.Model):
    date_created = models.DateField(auto_now=True)
    text = models.TextField()
    employee = models.ManyToManyField(Employee)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:25]
