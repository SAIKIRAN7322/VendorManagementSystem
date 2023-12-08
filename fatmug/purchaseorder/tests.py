from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import PurchaseOrder
from datetime import datetime
# Create your tests here.
class PurchaseOrderTest(APITestCase):
    # testcase for creating a new purchaseorder
    def test_register(self):
        _data={
                "vendor": 5,
                "delivery_date": "2023-12-08T08:31:00.941Z",
                "items": {},
                "status": "pending",
                "quantity": 2147483647,
                "quality_rating": 0,
                "issue_date": "2023-12-08T08:31:00.941Z",
                "acknowledgement_date": "2023-12-08T08:31:00.941Z"
                }
        _response = self.client.post('/api/purchase_orders/',data=_data,format='json')
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
    
    # testcase for retreiving list of purchaseorders
    def test_get_PurchaseOrder_list(self):
        _response = self.client.get('/api/purchase_orders/',format='json')
        self.assertEqual(_response.status_code,status.HTTP_200_OK)
        
    # testcase for retreiving a particular purchaseorder
    def test_get_purchase_order(self):
        _response = self.client.get('/api/purchase_orders/1',format='json')
        try :
            PurchaseOrder.objects.get(1)
            self.assertEqual(_response.status_code,status.HTTP_200_OK)
        except:
            self.assertEqual(_response.status_code,status.HTTP_404_NOT_FOUND)
            
    # testcase for updating a particular purchaseorder
    def test_put_PurchaseOrder(self):
        _data={
            'name':'test',
            'address':"test",
            'contact_details':"test"
        }
        try :
            _response = self.client.put('/api/purchase_orders/8',format='json',data=_data)
            PurchaseOrder=PurchaseOrder.objects.get(id=8)
            self.assertEqual(_response.status_code,status.HTTP_200_OK)
            self.assertEqual(_response.json(),PurchaseOrder)
        except:
            _response = self.client.put('/api/purchase_orders/8',format='json',data=_data)
            self.assertEqual(_response.status_code,status.HTTP_404_NOT_FOUND)
            
    # testcase for deleting a particular purchaseorder
    def test_del_purchase_order(self):
        try:
            PurchaseOrder.objects.get(id=8)
            _response = self.client.delete('/api/purchase_orders/8')
            self.assertEqual(_response.status_code,status.HTTP_204_NO_CONTENT)
        except:
            _response = self.client.delete('/api/purchase_orders/8')
            self.assertEqual(_response.status_code,status.HTTP_404_NOT_FOUND)