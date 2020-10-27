from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()

        order_text = request.GET.get('text', None)
        if order_text is not None:
            orders = orders.filter(text__icontains=order_text)

        orders_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)

    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Order.objects.all().delete()
        return JsonResponse({'message': '{} Orders were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)

        if request.method == 'GET':
            order_serializer = OrderSerializer(order)
            return JsonResponse(order_serializer.data)
        elif request.method == 'PUT':
            order_data = JSONParser().parse(request)
            order_serializer = OrderSerializer(order, data=order_data)
            if order_serializer.is_valid():
                order_serializer.save()
                return JsonResponse(order_serializer.data)
            return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            order.delete()
            return JsonResponse({'message': 'Order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Order.DoesNotExist:
        return JsonResponse({'message': 'The order does not exist'}, status=status.HTTP_404_NOT_FOUND)
