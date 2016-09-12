from django.http import HttpResponse
from twython import Twython, TwythonError
from myproject.utils.twitter_parser import Parser

def latest_tweet(request):
    """
        Gets latest tweet from the Twitter user specified in settings.
        Caches latest tweet for 10 minutes to reduce API calls
    """
    latest_tweet = cache.get('latest_tweet')
 
    if not latest_tweet:
        parser = Parser()
 
        twitter = Twython(settings.TWITTER_KEY,
                          settings.TWITTER_SECRET,
                          settings.OAUTH_TOKEN,
                          settings.OAUTH_TOKEN_SECRET)
        try:
            user_timeline = twitter.get_user_timeline(screen_name="silkstreamnet",count=3)
        except TwythonError as e:
            return {"latest_tweet": e}
 
        latest_tweet = user_timeline[0]
        latest_tweet['text'] = parser.parse(latest_tweet['text']).html
        cache.set('latest_tweet', latest_tweet, settings.TWITTER_TIMEOUT)
    return {'latest_tweet': latest_tweet}