from rest_framework import serializers
from purchaseorder.models import PurchaseOrder
class PurchaseOrderSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = PurchaseOrder
        fields = [
            "po_number",
            "vendor",
            "delivery_date",
            "items",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgement_date"
        ]
        read_only_fields = ["po_number"]
        extra_kwargs = {
            'vendor': {'required': True},
            'delivery_date': {'required': True},  
            'items': {'required': True},
            'quantity':{'required': True}
        }

    