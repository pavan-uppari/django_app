from rest_framework.test import APITestCase

from django.urls import reverse
from base.models import Item
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ItemTests(APITestCase):

    def setUp(self):

        #creating test superuser and setting authorization token

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create one item for testing
        self.item = Item.objects.create(name='Item 1', description='Description 1')

    def test_valid_get_item(self):
        
        url = reverse('get_item',kwargs={'item_id': self.item.id})
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data["id"] == self.item.id
        assert response.data["name"] == self.item.name
        assert response.data["description"] == self.item.description

    def test_invalid_get_item(self):

        url = reverse('get_item',kwargs={'item_id': 100})
        response = self.client.get(url)

        assert response.status_code == 404
        assert response.data == {'error': 'item not found'}
