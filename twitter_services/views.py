# django library imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
# third party imports
import tweepy

# setting up twitter authentications
auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                           settings.TWITTER_SECRET_KEY)

# setting up twitter tokens
auth.set_access_token(settings.TWITTER_CONSUMER_TOKEN,
                      settings.TWITTER_SECRET_TOKEN)

# initializing twitter authentication
api = tweepy.API(auth)


# function for index page requests handling
def retrieve_index_page(request):
    """
    Author - Aryan Jadon

    function which extracts all the tweets of the user using twitter api credentials
    tweets will gets stored in a dictionary objects for index page display.
    @param request: django request
    @return: renders index page with twitter account tweets
    """
    # getting all the tweets
    public_tweets = api.home_timeline()

    # creating two dictionaries
    context = {}
    all_tweets = {}

    # lopping through tweets extracted from api
    for tweet in public_tweets:
        # storing tweets information in dictionary
        all_tweets[tweet.id_str] = {'user_name': tweet.user.screen_name,  # twitter user name
                                    'created_at': tweet.created_at,  # tweet date
                                    'tweet': tweet.text}  # tweet text

    # updating the context dictionary
    context.update({'all_tweets': all_tweets})

    # rendering the dictionary to html page
    return render(request, 'index.html', context)


# function for create tweet request handling
def create_view(request):
    """
    Author - Aryan Jadon

    function which creates new tweet using post request

    @param request: django request data
    @return: redirects to index page with alert of create operation
    """
    # check if request is POST
    if request.method == "POST":
        # get the user tweet data from post request
        user_tweet = request.POST['user_tweet']

        # check for duplicate
        if check_for_duplicate(user_tweet):
            # create the tweet
            api.update_status(user_tweet)
            # update the django messages
            messages.success(request, 'Tweet Successfully Created!')
        else:
            # update the django messages
            messages.warning(request, 'Duplicated Tweet- Cannot be posted !!')

        # redirects to the index page, containing all tweets
        return redirect('index_page')
    else:
        # renders create tweet html page
        return render(request, 'create_tweet.html')


# function to check for duplicate tweet
def check_for_duplicate(tweet_text):
    """
    Author - Aryan Jadon

    function to check for duplicated tweet

    @param tweet_text: tweet data
    @return: boolean value
    """

    # get all tweets
    public_tweets = api.home_timeline()

    # loop through tweets
    for tweet in public_tweets:
        if tweet_text == tweet.text:
            # if already present return false
            return False

    # return true
    return True


# function for delete tweet request handling
def delete_view(request):
    """
    Author - Aryan Jadon

    function to delete the tweet using post request data
    @param request: django request
    @return: renders the request to index page
    """

    # check if request is POST
    if request.method == "POST":
        # get the tweet id from POST Request
        api.destroy_status(request.POST['tweet_id'])
        # update the django message
        messages.success(request, 'Tweet Successfully Deleted!')

    # renders to the index page containing all the tweets
    return redirect('index_page')
