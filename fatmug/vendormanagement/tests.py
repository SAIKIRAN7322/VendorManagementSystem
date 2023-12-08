
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Vendor

# Create your tests here.

class VendorTest(APITestCase):
    def test_register(self):
        _data={
            'name':'test',
            'address':"test",
            'contact_details':"test"
        }
        _response = self.client.post('/api/vendors/',data=_data,format='json')
        _data = _response.json()
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
    
    def test_get_vendor_list(self):
        _response = self.client.get('/api/vendors/',format='json')
        _data = _response.json()
        self.assertEqual(_response.status_code,status.HTTP_200_OK)
        
    def test_get_vendor(self):
        _response = self.client.get('/api/vendors/1',format='json')
        _data = _response.json()
        try :
            Vendor.objects.get(1)
            self.assertEqual(_response.status_code,status.HTTP_200_OK)
        except:
            self.assertEqual(_response.status_code,status.HTTP_404_NOT_FOUND)
            
    def test_put_vendor(self):
        _data={
            'name':'test',
            'address':"test",
            'contact_details':"test"
        }
        try :
            _response = self.client.put('/api/vendors/8',format='json',data=_data)
            vendor=Vendor.objects.get(id=8)
            self.assertEqual(_response.status_code,status.HTTP_200_OK)
            self.assertEqual(_response.json(),vendor)
        except:
            _response = self.client.put('/api/vendors/8',format='json',data=_data)
            self.assertEqual(_response.status_code,status.HTTP_404_NOT_FOUND)
            
    def test_del_vendor(self):
        _response = self.client.delete('/api/vendors/8')
        self.assertEqual(_response.status_code,status.HTTP_204_NO_CONTENT)
    
    def test_vendor_performance(self):
        try:   
            _response = self.client.get('/api/vendors/8')
            Vendor.objects.get(id=8)
            self.assertEqual(_response.status_code,status.HTTP_200_OK)
        except:
            _response = self.client.get('/api/vendors/8')
            self.assertEqual(_response.status_code,status.HTTP_404_NOT_FOUND)
            


            
            







# class VendorTestCase(APITestCase):
#     def setUp(self):
#         self.url = reverse('vendor_list_create')
#         self.valid_data = {'name':"test",'contact_details':"7984848484",'address':"opposite banglore marathalli area"}
#         self.invalid_data = {'name':"test",'contact_details':"7984848484"}
        
        
#     def test_vendor_create_valid_object(self):
#         response = self.client.post(self.url,self.valid_data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
#         self.assertEqual(Vendor.objects.count(),1) 
    
#     def test_vendor_create_invalid_object(self):
#         response = self.client.post(self.url, self.invalid_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(Vendor.objects.count(), 0)  # Ensure no object is created  
    
#     def test_list_objects(self):
#         # Assuming you have some objects created in the database
#         Vendor.objects.create(name='test1', contact_details='test1',address='test1')
#         Vendor.objects.create(name='test2', contact_details='test2',address='test2')
#         Vendor.objects.create(name='test3', contact_details='test3',address='test3')
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), Vendor.objects.count())