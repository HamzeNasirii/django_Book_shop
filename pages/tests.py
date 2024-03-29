from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.sataus_code, 200)

    def test_home_page_templates_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
# Create your tests here.
