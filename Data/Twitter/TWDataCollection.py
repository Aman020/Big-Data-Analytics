
import tweepy as tweepy
import pandas as pd
import csv



consumerApikey = "XcHOAVRMJa0PnGMhBKsbZOF3W"
consumerApiSecretKey = "06gmf6S12GbulHThDQA3AlWB5el2e8HbVrYdlqIHKp6vTf2ucf"
accessToken = "897511905970987008-WdYbvfk4wKWlUceed1EFLvXpaNhw4gJ"
acccessSecretToken = "MXp4vCe3eHKPQREFkNI4BlBoeNqgqi4QGNpzZd79At8fV"

auth = tweepy.OAuthHandler(consumerApikey, consumerApiSecretKey)
auth.set_access_token(accessToken, acccessSecretToken)
api = tweepy.API(auth, wait_on_rate_limit=True)
twKeyword = "#governmentshutdown -filter:retweets"
dateRange = "2019-01-01"
# tweets = tweepy.Cursor(api.search, q =search_words,lang="en",since=date_since).items(100)
#

csvFile = open('twittedData.csv','a')
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,
                           q=twKeyword,since=dateRange,
                           include_entities=True,
                           lang="en").items(1):
    csvWriter.writerow([tweet.created_at, tweet.text])

csvFile.close()
