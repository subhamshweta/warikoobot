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

userID = 'FitFounder' # Change 'FitFounder' to any other twitter username

while True:
    tweets = api.user_timeline(screen_name=userID, count=10, include_rts = False, exclude_replies = True, tweet_mode = 'extended')
    
    try:
        for info in tweets[:1]:
            newtweet = info.full_text 
            print("New Tweet " + newtweet)
            print("Length of tweet is " + str(len(newtweet)))
            print("\n")
            #api.update_status(newtweet)
            time.sleep(300)
        
        if len(newtweet) < 260:
            api.update_status('"%s" - @%s' %(newtweet,userID))
            # api.update_status(newtweet)
            print("Tweeted")
            print("\n")
            time.sleep(500)
    
        else:
            print("Length of Tweet is more than 260 characters")
            print("\n")

    except Exception as e:
        print(e)
        time.sleep(1800)
