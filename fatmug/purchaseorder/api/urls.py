from django.urls import path
from .views import PurchaseOrderCreateView,PurchaseOrderUpdateApiView,PurchaseOrderAcknowledgeApiView
urlpatterns = [
    path('',PurchaseOrderCreateView.as_view()),
    path('<pk>',PurchaseOrderUpdateApiView.as_view()),
    path("<pk>/acknowledge",PurchaseOrderAcknowledgeApiView.as_view())
    
    
    
]