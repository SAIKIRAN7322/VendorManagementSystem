from django.db import models
import random
from datetime import timedelta
from django.db.models import F, ExpressionWrapper, fields
# Create your models here.

default_blank_nullF = dict(default=None, blank=False, null=False)
default_blank_nullT = dict(default=None, blank=True, null=True)

class Vendor(models.Model):
    name = models.CharField(max_length=100,**default_blank_nullF)
    contact_details = models.TextField(**default_blank_nullF)
    address = models.TextField(**default_blank_nullF)
    vendor_code = models.CharField(max_length=150, **default_blank_nullT)
    on_time_delivery_rate = models.FloatField(null=True, blank=True, default=None)
    quality_rating_avg = models.FloatField(null=True, blank=True, default=None)
    average_response_time = models.FloatField(null=True, blank=True, default=None)
    fulfillment_rate = models.FloatField(null=True, blank=True, default=None)        
    
    
    def calculate_on_time_deliveryrate(self,*args,**kwargs):
        #retreiving all completed status po objects related to vendor
        total_completed_deliveries = self.purchaseorder_set.filter(status="completed")
        on_time_deliveries = total_completed_deliveries.filter(status = "completed",acknowledgement_date__lte=F("delivery_date"))
        on_time_delivery_rate = (on_time_deliveries.count()/total_completed_deliveries.count())*100 if total_completed_deliveries.count()>0 else 0
        self.on_time_delivery_rate = on_time_delivery_rate
        super(Vendor, self).save()
        return on_time_delivery_rate
    
    def calculate_quality_rating_average(self,*args,**kwargs):
        #retreiving all completed status po objects related to vendor
        completed_deliveries = self.purchaseorder_set.filter(status="completed")
        quality_ratings = completed_deliveries.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
        quality_rating_average = sum(quality_ratings)/len(quality_ratings) if len(quality_ratings)>0 else 0
        self.quality_rating_avg = quality_rating_average
        super(Vendor, self).save()
        return quality_rating_average
    
    def calculate_average_response_time(self):
        #retreiving all completed status po objects related to vendor
        completed_orders = self.purchaseorder_set.filter(status = "completed")
        response_times = completed_orders.exclude(acknowledgement_date__isnull=True).annotate(
            response_time=ExpressionWrapper(F('acknowledgement_date') - F('issue_date'), output_field=fields.DurationField())
        ).values_list('response_time', flat=True)
        average_response_time = sum(response_times, timedelta()) / len(response_times) if len(response_times) > 0 else 0
        self.average_response_time = average_response_time
        super(Vendor, self).save()
        return average_response_time
    
    def calculate_fulfillment_rate(self):
        #retreiving all completed status po objects related to vendor
        completed_orders = self.purchaseorder_set.filter(status='completed')
        fulfilled_orders = completed_orders.filter(issue_date__lte=F('acknowledgement_date'))
        total_completed_orders = completed_orders.count()
        fulfillment_rate = (fulfilled_orders.count() / total_completed_orders) * 100 if total_completed_orders > 0 else 0
        self.fulfillment_rate = fulfillment_rate
        super(Vendor, self).save()
        return fulfillment_rate
    
    def save(self,*args,**kwargs):
        if not self.vendor_code:
            vendor_code = 'VC'+ str(random.randint(1000, 9999))
            while Vendor.objects.filter(vendor_code=vendor_code).exists():
                vendor_code = 'VC'+ str(random.randint(1000, 9999))
            self.vendor_code=vendor_code
        super(Vendor, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name 
    
     
    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        

    
    
    
    
    
