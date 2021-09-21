from django.shortcuts import render
from django.shortcuts import redirect
import tweepy

auth = tweepy.OAuthHandler('DbwTjGUxXot2M4rNEEv2NulRR',
                           '4Hk8jJr133Xt7tqV4DQcB1UXnRNrwf0c2ygLUkMUAtqS9FPsXQ')

auth.set_access_token('1440090791230070785-sExgZJz7qoE6BSw5dHVkdAqtdtI9Lw',
                      '9zerxO7vkKzKgKAfMLjd3aual0D3SrpdSwxPvLNRRvuHO')

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
        return redirect('index_page')
    else:
        return render(request, 'create_tweet.html')


def delete_view(request):
    if request.method == "POST":
        api.destroy_status(request.POST['tweet_id'])
    return redirect('index_page')
