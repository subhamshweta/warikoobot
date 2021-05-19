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

while True:
    user = api.get_user('subham_shweta')  # Change 'subham_shweta' to any other twitter username
    copy = user.status.text
    try:
        api.update_status(copy)         # Post copied tweet
        print('Paste')
        time.sleep(5)

    except Exception as e:
        print(e)
        time.sleep(10)
        continue
