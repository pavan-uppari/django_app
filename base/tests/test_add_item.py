from rest_framework.test import APITestCase

from django.urls import reverse
from base.models import Item
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ErrorDetail

class ItemTests(APITestCase):

    def setUp(self):

        #creating test superuser and setting authorization token

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')


    def test_add_item(self):
        
        url = reverse('add_item')
        data = {
            'name': 'Item',
            'description': 'Description'
        }
        response = self.client.post(url, data, format="json")

        assert response.status_code == 201
        assert response.data.pop("id") == 1
        assert response.data == data

    def test_add_duplicate_name(self):

        # Create one item
        created_item = Item.objects.create(name='Item 1', description='Description 1')
        
        url = reverse('add_item')
        data = {
            'name': created_item.name,
            'description': 'Description'
        }
        response = self.client.post(url, data, format="json")

        assert response.status_code == 400
        assert response.json() == {'name': ['item with this name already exists.']}

