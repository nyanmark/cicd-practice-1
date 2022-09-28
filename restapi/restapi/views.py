from http.client import SERVICE_UNAVAILABLE
from unicodedata import decimal
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .serializers import DegreesInputSerializer, PastDegreesToRadiansResultSerializer
from .models import PastDegreesToRadiansResult
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import math

@cache_page(10)
def past_results(request):
    model_data = PastDegreesToRadiansResult.objects.all()
    serializer = PastDegreesToRadiansResultSerializer(model_data, many=True)
    return JsonResponse({"past_results": serializer.data})

def decimal_degrees(seconds, minutes, degrees):
    decimal_degrees = float(degrees) + float(minutes)/60 + float(seconds)/3600
    return decimal_degrees

def degrees_to_radians(decimal_degrees):
    radians = decimal_degrees * (math.pi/180)
    return radians

@api_view(['POST'])
def conversion(request):
    input_serializer = DegreesInputSerializer(data=request.data)
    if input_serializer.is_valid():
        degrees_result = decimal_degrees(input_serializer.data['seconds'], input_serializer.data['minutes'], input_serializer.data['degrees'])
        degrees_result_formatted = float("{:.8f}".format(degrees_result))
        radians_result = degrees_to_radians(degrees_result_formatted)
        radians_result_formatted = float("{:.12f}".format(radians_result))
        serializer_data = {'seconds_input': request.data['seconds'], 'minutes_input': request.data['minutes'], 'degress_input': request.data['degrees'], 'degress_result': degrees_result_formatted, 'radians_output': radians_result_formatted}
        storage_serializer = PastDegreesToRadiansResultSerializer(data=serializer_data)
        if storage_serializer.is_valid():
            storage_serializer.save()
            return Response(storage_serializer.data, status=status.HTTP_200_OK)
