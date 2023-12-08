from django.db import models
from vendormanagement.models import Vendor
import random

# Create your models here.
default_blank_nullF = dict(default=None, blank=False, null=False)
default_blank_nullT = dict(default=None, blank=True, null=True)

class PurchaseOrder(models.Model):
    status=[("pending","pending"),("completed","completed"),("cancelled","cancelled")]
    po_number = models.CharField(max_length=150, **default_blank_nullT)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(**default_blank_nullT)
    items = models.JSONField()
    quantity = models.IntegerField(**default_blank_nullT)
    status = models.CharField(choices=status,default=status[0][0])
    quality_rating = models.FloatField(null=True, blank=True, default=None)
    issue_date = models.DateTimeField(**default_blank_nullT)
    acknowledgement_date = models.DateTimeField(**default_blank_nullT)
    def save(self,*args,**kwargs):
        if not self.po_number:
            po_number = 'PO'+ str(random.randint(1000, 9999))
            while PurchaseOrder.objects.filter(po_number=po_number).exists():
                po_number = 'PO'+ str(random.randint(1000, 9999))
            self.po_number=po_number
        super(PurchaseOrder, self).save(*args, **kwargs)
    def __str__(self):
        return self.po_number
    class Meta:
        verbose_name = "PurchaseOrder"
        verbose_name_plural = "PurchaseOrders"