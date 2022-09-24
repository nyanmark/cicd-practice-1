from django.db import models

class PastDegreesToRadiansResult(models.Model):
    seconds_input = models.DecimalField(max_digits=4, decimal_places=2)
    minutes_input = models.DecimalField(max_digits=4, decimal_places=2)
    degress_input = models.DecimalField(max_digits=6, decimal_places=2)
    degress_result = models.DecimalField(max_digits=12, decimal_places=8)
    radians_output = models.DecimalField(max_digits=14, decimal_places=12)
