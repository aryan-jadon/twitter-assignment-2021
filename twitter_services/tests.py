import tweepy
from django.test import TestCase
from django.urls import reverse, resolve
import json
from django.conf import settings
import tweepy

# auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
#                            settings.TWITTER_SECRET_KEY)
#
# auth.set_access_token(settings.TWITTER_CONSUMER_TOKEN,
#                       settings.TWITTER_SECRET_TOKEN)
#
# api = tweepy.API(auth)


class ViewsTestCase(TestCase):

    # def test_index_loads_properly(self):
    #     """The index page loads properly"""
    #     response = self.client.get('http://127.0.0.1:8000/')
    #     # response status code 200 - Running OK
    #     self.assertEqual(response.status_code, 200)

    def test_retrieve_index_page(self):
        response = self.client.get(reverse('index_page'))
        print(response)
        self.assertEqual(response.status_code, 200)

    #
    def test_create_page(self):
        response = self.client.get(reverse('create_tweet'))
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_create_tweet_post(self):
        response = self.client.post(reverse('create_tweet'), data={'user_tweet': 'test tweet check211'}, )
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

    def test_create_tweet_specialCharacters_post(self):
        response = self.client.post(reverse('create_tweet'), data={'user_tweet': 'test tweet,w!thspeci@l#ch@_check1'}, )
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

    def test_create_duplicate_tweet_post(self):
        response1 = self.client.post(reverse('create_tweet'), data={"user_tweet": 'test tweet check211'}, )
        print(response1.status_code)
        self.assertEqual(response1.status_code, 302)

    def test_create_page_post_no_data(self):
        response = self.client.post(reverse('create_tweet'), data={"user_tweet": ''}, )
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

    # delete is not working @Aryan Can you pls check it
    # def test_delete_tweet(self):
    #     response = self.client.post(reverse('create_tweet'), data={'user_tweet': 'test delete'}, )
    #     public_tweets = api.home_timeline()
    #     tweet_id = ''
    #     for tweet in public_tweets:
    #         if 'test delete' == tweet.text:
    #             tweet_id = tweet.id
    #     response1 = self.client.delete(reverse('delete_tweet'), data={'tweet_id': tweet_id})
    #     print(response1.status_code)
    #     self.assertEqual(response1.status_code, 302)
