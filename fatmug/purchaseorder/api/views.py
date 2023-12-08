from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from purchaseorder.models import PurchaseOrder
from .serializers import PurchaseOrderSerailizer
from rest_framework.response import Response
from datetime import datetime
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.authentication import JWTAuthentication

# view for creating and retrieving list of purchaseorders
class PurchaseOrderCreateView(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerailizer
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        query_params = self.request.query_params
        vendor_id = query_params.get('vendor', False)
        if vendor_id:
            return PurchaseOrder.objects.filter(vendor_id=vendor_id)
        else:
            return PurchaseOrder.objects.all()
# view for updating a purchaseorder
class PurchaseOrderUpdateApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerailizer

# view for acknowledging a purchaseorder by vendor
class PurchaseOrderAcknowledgeApiView(RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerailizer
    authentication_classes=[JWTAuthentication]
    def retrieve(self, request,*args,**kwargs):
        instance = self.get_object()
        if not instance.acknowledgement_date:
            instance.acknowledgement_date=datetime.now()
            instance.save()
            instance.vendor.calculate_average_response_time()
        else:
            return Response({"message":"The purchase order has been already acknowledged by the vendor"},status = HTTP_400_BAD_REQUEST)
        return super().update(request,*args, **kwargs)
    
    
                
        

        
    

        
