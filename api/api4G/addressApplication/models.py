from django.db import models


class OperatorTable(models.Model):
    operator_name = models.CharField(max_length=20)
    long = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    is_2g = models.BooleanField()
    is_3g = models.BooleanField()
    is_4g = models.BooleanField()

    def __str__(self):
        return "{} : x : {} y : {}".format(self.operator_name,
                                           self.lon,
                                           self.lat)