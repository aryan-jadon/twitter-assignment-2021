from django.test import TestCase
from django.urls import reverse
from django.conf import settings
# third party imports
import tweepy


# Authors - Shreya and Harika
class ViewsTestCase(TestCase):
    # Request Test Case - 1
    def test_index_page(self):
        """ index page loads properly """
        response = self.client.get(reverse('index_page'))

        # response status code 200 - Running OK
        self.assertEqual(response.status_code, 200)

    # Request Test Case - 2
    def test_create_tweet_page(self):
        """ create tweet page loads properly """
        response = self.client.get(reverse('create_tweet'))

        # response status code 200 - Running OK
        self.assertEqual(response.status_code, 200)

    # Template Used Test Case - 1
    def test_index_view_uses_correct_template(self):
        """ index html template loads properly """
        response = self.client.get(reverse('index_page'))

        # response status code 200 - Running OK
        self.assertEquals(response.status_code, 200)

        # checking template used
        self.assertTemplateUsed(response, 'index.html')

    # Template Used Test Case - 2
    def test_create_view_uses_correct_template(self):
        """ create tweet html template loads properly """
        response = self.client.get(reverse('create_tweet'))

        # response status code 200 - Running OK
        self.assertEquals(response.status_code, 200)

        # checking template used
        self.assertTemplateUsed(response, 'create_tweet.html')

    # Checking HTML Response
    def test_about_page_does_not_contain_incorrect_html(self):
        """ testing html strings on index page """
        # sending request to index page
        response = self.client.get(reverse('index_page'))

        # checking html data
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    # Testing CRUD Operations
    def test_crud_operation_on_tweet_post(self):
        """ CRUD Operations Test """

        # setting up twitter authentications
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                                   settings.TWITTER_SECRET_KEY)

        # setting up twitter tokens
        auth.set_access_token(settings.TWITTER_CONSUMER_TOKEN,
                              settings.TWITTER_SECRET_TOKEN)

        # initializing twitter authentication
        api = tweepy.API(auth)

        # timeline
        public_tweets = api.home_timeline()

        # get numbers of tweets present in timeline
        number_of_tweets_in_profile = len(public_tweets)

        # storing all tweet id's
        all_tweet_ids = [tweet.id_str for tweet in public_tweets]

        # checking number of tweets
        self.assertEqual(number_of_tweets_in_profile, len(all_tweet_ids))

        # sending create tweet request with data
        response = self.client.post(reverse('create_tweet'),
                                    data={'user_tweet': 'creating tweet for test case'}, )

        # checking redirected response
        self.assertEqual(response.status_code, 302)

        # timeline
        updated_public_tweets = api.home_timeline()

        # storing all tweet id's
        updated_all_tweet_ids = [tweet.id_str for tweet in updated_public_tweets]

        # timeline
        updated_public_tweets = api.home_timeline()

        # this should not match with updated tweets length
        self.assertNotEqual(len(public_tweets), len(updated_public_tweets))

        # Create tweet tests done

        # delete tweet test process starts
        for tweet_id in updated_all_tweet_ids:
            if tweet_id not in all_tweet_ids:
                added_tweet_id = tweet_id

        # sending delete tweet request with data
        response = self.client.post(reverse('delete_tweet'),
                                    data={'tweet_id': added_tweet_id}, )

        # checking redirected response
        self.assertEqual(response.status_code, 302)

        # timeline
        updated_public_tweets = api.home_timeline()

        # this should match with updated tweets length
        self.assertEqual(len(public_tweets), len(updated_public_tweets))
        # delete test completed
