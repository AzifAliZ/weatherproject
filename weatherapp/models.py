from django.db import models

class SearchHistory(models.Model):
    city = models.CharField(max_length=50)
    temperature = models.FloatField()
    windspeed = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
