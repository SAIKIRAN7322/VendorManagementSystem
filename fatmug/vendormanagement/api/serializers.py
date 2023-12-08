from rest_framework import serializers
from vendormanagement.models import Vendor

# serializer for creating a vendor
class Vendorserializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = (
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate"
        )
        read_only_fields = ['vendor_code']
        extra_kwargs = {
            'name': {'required': True},
            'address': {'required': True},  
            'contact_details': {'required': True},
        }

        

# serializer for retreiving performance of a vendor
class VendorPerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.SerializerMethodField()
    quality_rating_avg = serializers.SerializerMethodField()
    average_response_time = serializers.SerializerMethodField()
    fulfillment_rate = serializers.SerializerMethodField()
    class Meta:
        model = Vendor
        fields =[
            "id",
            "name",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate"
        ]
    def get_on_time_delivery_rate(self,vendor_instance):
        on_time_delivery_rate = vendor_instance.calculate_on_time_deliveryrate()
        return on_time_delivery_rate
    def get_quality_rating_avg(self,vendor_instance):
        quality_rating_avg = vendor_instance.calculate_quality_rating_average()
        return quality_rating_avg
    def get_average_response_time(self,vendor_instance):
        average_response_time = vendor_instance.calculate_average_response_time()
        return average_response_time
    def get_fulfillment_rate(self,vendor_instance):
        fulfillment_rate = vendor_instance.calculate_fulfillment_rate()
        return fulfillment_rate
        