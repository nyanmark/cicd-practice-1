from rest_framework import serializers
from .models import PastDegreesToRadiansResult

class PastDegreesToRadiansResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastDegreesToRadiansResult
        fields = ['seconds_input', 'minutes_input', 'degress_input', 'degress_result', 'radians_output']

class DegreesInputSerializer(serializers.Serializer):
    seconds = serializers.DecimalField(max_digits=4, decimal_places=2)
    minutes = serializers.DecimalField(max_digits=4, decimal_places=2)
    degrees = serializers.DecimalField(max_digits=6, decimal_places=2)

