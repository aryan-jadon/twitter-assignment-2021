from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
import tweepy

auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                           settings.TWITTER_SECRET_KEY)

auth.set_access_token(settings.TWITTER_CONSUMER_TOKEN,
                      settings.TWITTER_SECRET_TOKEN)

api = tweepy.API(auth)


# Create your views here.
def retrieve_index_page(request):
    public_tweets = api.home_timeline()
    context = {}
    all_tweets = {}
    for tweet in public_tweets:
        all_tweets[tweet.id_str] = {'user_name': tweet.user.screen_name,
                                    'created_at': tweet.created_at,
                                    'tweet': tweet.text}
    context.update({'all_tweets': all_tweets})
    return render(request, 'index.html', context)


def create_view(request):
    if request.method == "POST":
        user_tweet = request.POST['user_tweet']
        api.update_status(user_tweet)
        messages.success(request, 'Tweet Successfully Created!')
        return redirect('index_page')
    else:
        return render(request, 'create_tweet.html')


def delete_view(request):
    if request.method == "POST":
        api.destroy_status(request.POST['tweet_id'])
        messages.success(request, 'Tweet Successfully Deleted!')
    return redirect('index_page')
