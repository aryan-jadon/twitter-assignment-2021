from django.test import TestCase


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


# which html pages are we using - index.html , create_tweet.html
