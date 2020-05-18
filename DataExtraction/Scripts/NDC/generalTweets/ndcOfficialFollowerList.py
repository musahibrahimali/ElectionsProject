import csv
import tweepy
from nltk.tokenize import TweetTokenizer
from tweepy import RateLimitError
from DataExtraction.Scripts import twitter_credentials
import time

tknzr = TweetTokenizer(strip_handles=True)

CONSUMER_KEY = twitter_credentials.CONSUMER_KEY
CONSUMER_SECRET = twitter_credentials.CONSUMER_SECRET
ACCESS_TOKEN = twitter_credentials.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_credentials.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('../../../CollectedData/NDC/NDCOfficialFollowerList.csv', 'a', encoding="utf-16")
csvWriter = csv.writer(csvFile)
csvWriter.writerow([
    "id", "screen name", "name", "followers count", "friends count", "listed count", "location"
])

# get the friends list of the user

for user in tweepy.Cursor(api.friends, screen_name="OfficialNDCGh").items():
    try:
        with open('../../../CollectedData/NDC/NDCOfficialFollowerList.csv', 'a', encoding="utf-16") as csvFile:
            csvWriter.writerow([
                user.id, user.screen_name, user.name, user.followers_count, user.friends_count, user.listed_count,
                user.location
            ])
        print(user.screen_name)
    except UnicodeEncodeError:
        csvWriter.writerow([
            str(user.id), str(user.screen_name), str(user.name), str(user.followers_count), str(user.friends_count),
            str(user.listed_count), str(user.location)
        ])
    except RateLimitError:
        print("rate Limit Exceeded, wait for a while")
        time.sleep(60 * 15)
