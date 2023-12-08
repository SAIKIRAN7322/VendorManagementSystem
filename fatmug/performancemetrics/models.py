from django.db import models
from vendormanagement.models import Vendor
# Create your models here.
class PerformanceMetrics(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)
    def __str__(self):
        return self.vendor.name
    class Meta:
        verbose_name="PerformanceMetrics"
        verbose_name_plural = "PerformanceMetrics"
    