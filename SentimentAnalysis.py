from textblob import TextBlob
import sys
import time
import tweepy

#API keys and secrets to connect to Twitter Developer application

api_key = ""
api_secret = ""
access_token = ""
access_secret = ""

#define the authentication handler and plug in our keys to tweepy

auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_secret)
auth_handler.set_access_token(access_token, access_secret)

api = tweepy.API(auth_handler)

#Define what we want to search for and how many tweets we want to parse

print('Welcome to my Twitter Sentiment Analysis Tool made with Python')
time.sleep(1)
search_term = input('Input a word or phrase you would like to perform the analysis on:')
time.sleep(2)
num_tweets = input('Input how many tweets you would like to perform the analysis on: ')


polarity = 0

#Use the tweepy cursor object to search https://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
#use the search method with our api, then pass in the search term, language, and # of tweets in the items.
tweets = tweepy.Cursor(api.search, q = search_term, lang = 'en').items(int(num_tweets))

positive = 0
negative = 0
neutral = 0

#remove any RT or names of users because we just want the contents of the tweet.

print('Loading...')
time.sleep(0.5)
print('Loading...')
time.sleep(0.5)
print('Loading...')
time.sleep(1)

for tweet in tweets:
    output = tweet.text.replace('RT', '')
    if output.startswith(' @'):
        position = output.index(':')
        output = output[position + 2:]
    if output.startswith('@'):
        position = output.index(' ')
        output = output[position + 1:]
    #perform textblob sentiment analysis on the tweets
    SentAnalysis = TextBlob(output)
    polarity += SentAnalysis.polarity
    #find the # of positive and negative tweets
    tweetPolarity = SentAnalysis.polarity

    if tweetPolarity > 0.5:
        positive += 1
    elif tweetPolarity < 0.5:
        negative += 1
    else:
        neutral += 1

print('Loading...')
time.sleep(0.5)
print('Loading...')
time.sleep(0.5)
print('Loading...')
time.sleep(3)

if polarity > 15:
    print(f'On Twitter, {search_term} has a very positive sentiment with a polarity of {polarity}.')
    print('In total, there are:')
    print(f'{positive} positive tweets')
    print(f'{negative} negative tweets')
    print(f'{neutral} neutral tweets')
elif 10 < polarity < 15:
    print(f'On Twitter, {search_term} has a somewhat positive sentiment with a polarity of {round(polarity, 3)}.')
    print('In total, there are:')
    print(f'{positive} positive tweets')
    print(f'{negative} negative tweets')
    print(f'{neutral} neutral tweets')
elif 5 < polarity < 10:
    print(f'On Twitter, {search_term} has a somewhat negative sentiment with a polarity of {round(polarity, 3)}.')
    print('In total, there are:')
    print(f'{positive} positive tweets')
    print(f'{negative} negative tweets')
    print(f'{neutral} neutral tweets')
else:
    print(f'On Twitter, {search_term} has a very negative sentiment with a polarity of {round(polarity, 3)}.')
    print('In total, there are:')
    print(f'{positive} positive tweets')
    print(f'{negative} negative tweets')
    print(f'{neutral} neutral tweets')
