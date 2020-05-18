import csv
import tweepy
from nltk.tokenize import TweetTokenizer
from tweepy import RateLimitError

from DataExtraction.Scripts import twitter_credentials
import time

tknzr = TweetTokenizer(strip_handles=True)

access_token = twitter_credentials.ACCESS_TOKEN
access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET
consumer_key = twitter_credentials.CONSUMER_KEY
consumer_secret = twitter_credentials.CONSUMER_SECRET

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('../../../CollectedData/NPP/RunningMateTimeLineTweets.csv', 'a', encoding="utf-16")
csvWriter = csv.writer(csvFile)
csvWriter.writerow([
    "Date", "Id", "Text", "Likes", "Re-Tweets", "Location"
])

for tweet in tweepy.Cursor(api.user_timeline, screen_name='MBawumia', tweet_mode="extended").items():
    try:
        full_text = tweet.full_text
        full_text = ' '.join(tknzr.tokenize(full_text))
        csvWriter.writerow([
            tweet.created_at, tweet.id, full_text, tweet.favorite_count, tweet.retweet_count, tweet.user.location
        ])
        print(full_text)
    except RateLimitError:
        time.sleep(60 * 15)
    except UnicodeEncodeError:
        pass
