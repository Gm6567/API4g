from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse

class Api4gTests(TestCase):
    @patch("addressApplication.views.get_nearest_operators", 
    return_value={"Orange": {"2G" : True, "3G": False, "4G": True}})
    def test_view_with_correct_address(self, mocked_operators):
        resp = self.client.post(reverse("api"), {"id": "11 rue des pyrénées, 75020"})
        self.assertTrue("Orange" in resp.data["id"])

    @patch("addressApplication.views.get_nearest_operators", 
    return_value={"Orange": {"2G" : True, "3G": False, "4G": True}})
    def test_view_with_wrong_address(self, mocked_operators):
        resp = self.client.post(reverse("api"), {"id": "11 rue des pyrénées"})
        self.assertTrue("error" in resp.data["id"])

    @patch("addressApplication.views.get_nearest_operators", 
    return_value={"Orange": {"2G" : True, "3G": False, "4G": True}})
    def test_view_with_empty_json(self, mocked_operators):
        resp = self.client.post(reverse("api"), {})
        self.assertEqual(resp.data, {})