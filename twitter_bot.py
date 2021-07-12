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

userID = 'trendimemes' # Change 'trendimemes' to any other twitter username

while True:
    tweets = api.user_timeline(screen_name=userID, count=10, include_rts = False, tweet_mode = 'extended')
    
    try:
        for info in tweets[:1]:
            newtweet = info.full_text 
            print("New Tweet " + newtweet)
            
            #api.update_status(newtweet)
            api.update_status('"%s" - @%s' %(newtweet,userID))
            time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
        continue

