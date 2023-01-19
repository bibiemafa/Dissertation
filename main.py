import snscrape.modules.twitter as sntwitter
import pandas as pd

from time import sleep

tweet_data = []
username = input("Enter the user you want :.... ")
tweet_limit = int(input("Enter the number of tweets you want :.... "))

for i, tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
    if i > tweet_limit:
        break
    tweet_data.append([tweets.date, tweets.content, tweets.username, tweets.url])
data = pd.DataFrame(tweet_data, columns=['Date', 'Tweet', 'Username', 'Url'])
data.to_csv(f'{username}.csv', index=False, encoding='utf-8')
