from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        # response status code 200 - Running OK
        self.assertEqual(response.status_code, 200)

    def test_tweet_page_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/create/')
        # response status code 200 - Running OK
        self.assertEqual(response.status_code, 200)

# Template Test Cases
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertContains(response, '<h1>Welcome to Twitter! All Tweets!</h1>')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
