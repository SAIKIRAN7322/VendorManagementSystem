from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import PurchaseOrder
from performancemetrics.models import PerformanceMetrics


@receiver(pre_save,sender=PurchaseOrder)
def purchaseorder_pre_save(sender,instance,**kwargs):
    previous_state_of_instance = PurchaseOrder.objects.get(id=instance.id)
    print("previous state",previous_state_of_instance)
    print("present state",instance)