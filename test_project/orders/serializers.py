from rest_framework import serializers
from .models import Order
from customers.models import Customer
from employees.models import Employee


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'full_name',
            'phone_number',
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'full_name',
            'position',
        )


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id',
                  'date_created',
                  'text',
                  'employee',
                  'customer',)
