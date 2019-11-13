import config
import tweepy

auth = config.auth()

credential = tweepy.OAuthHandler(auth["API"], auth["API_SECRET"])
credential.set_access_token(auth["TOKEN"], auth["TOKEN_SECRET"])

api = tweepy.API(credential, wait_on_rate_limit=True)

while(True):
    try:
        for tweet in tweepy.Cursor(
                api.search, q="#100DaysOfCode", count=1, lang="en", since="2019-11-13").items():
            api.create_favorite(tweet.id)
    except Exception:
        print('Exception')
