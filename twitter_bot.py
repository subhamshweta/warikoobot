import tweepy
from os import environ
import time

CONSUMER_KEY = environ['CONSUMER_KEY'] 
CONSUMER_SECRET = environ['CONSUMER_SECRET'] 
ACCESS_KEY = environ['ACCESS_KEY']      
ACCESS_SECRET = environ['ACCESS_SECRET']

# To get above keys apply for twitter developer account and make an app.

def OAuth():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET )
        auth.set_access_token(ACCESS_KEY,ACCESS_SECRET )
        return auth
    except Exception as e:
        return e

auth = OAuth()
api = tweepy.API(auth)

user_name = 'trendimemes' # Change 'FitFounder' to any other twitter username

 # all full tweets (with full_text). Without it, long tweets

while True:
    user = api.get_user(user_name)  
    copy = user.status.text
    try:
        api.update_status(str('"%s" - @%s'.full_text %(copy,user_name))         # Post copied tweet
        print('Pasted')
        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
        continue

