from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveAPIView
from .serializers import Vendorserializer,VendorPerformanceSerializer
from vendormanagement.models import Vendor
from rest_framework_simplejwt.authentication import JWTAuthentication


#Api view for list of vendors and creating a vendor
class VendorApiView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = Vendorserializer
    queryset = Vendor.objects.all()
    
#Api view for retreiving a vendor using id and updating,deleting
class VendorupdateApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = Vendorserializer
    queryset = Vendor.objects.all()

#Api view for retreiving a vendor performance using id
class VendorPerformanceMetricsApiView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = VendorPerformanceSerializer
    queryset = Vendor.objects.all()