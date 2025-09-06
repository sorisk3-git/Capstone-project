from django.test import TestCase
from Restaurant.models import MenuItem
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.serializers import MenuItemSerializer

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Burger", price=50, inventory=200)
        self.item3 = MenuItem.objects.create(title="Pizza", price=120, inventory=150)

    def test_getall(self):
        response = self.client.get('/menu/')  # Adjust this URL to match your actual endpoint
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)