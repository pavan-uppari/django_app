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

        # Create some items for testing
        Item.objects.create(name='Item 1', description='Description 1')
        Item.objects.create(name='Item 2', description='Description 2')

    def test_get_items(self):
        
        url = reverse('get_items')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)