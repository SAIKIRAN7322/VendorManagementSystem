from django.urls import path
from .views import VendorApiView,VendorupdateApiView,VendorPerformanceMetricsApiView

urlpatterns = [
    
    path("",VendorApiView.as_view(),name='vendor_list_create'),
    path("<pk>",VendorupdateApiView.as_view()),
    path("<pk>/performance",VendorPerformanceMetricsApiView.as_view())
]