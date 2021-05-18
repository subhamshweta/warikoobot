import tweepy
import time

consumer_key = 'Fls5Egf4Y8AnbjVnPtsUfdhWv'
consumer_secret = '2mJdCvgfYosMnqWYSakzL8Tf5bltz21ejr9Kh6uqRRflTCog3C'
access_token = '1394535816915943427-6pRvdE0VP7gaUGV5vKmRhatrVvJAAH'
access_token_secret = 'ElL7NEIOFz7XjJXM8iXKKXBGHeI4K9JNJjCeULlD1CTnw'

# To get above keys apply for twitter developer account and make an app.

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
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
