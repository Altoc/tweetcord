import twitterAuth
import time
import tweepy
from time import sleep

api = twitterAuth.api

def twitterLookup(query, count):
	tweets_list = [];
	resultTweet = "";
	try:
		for tweet in api.search_tweets(q=query, tweet_mode='extended', count=count):
			tweets_list.append((tweet.user.name, tweet.full_text))
	except BaseException as e:
		print('failed on_stated,', str(e))
		time.sleep(2)
	if len(tweets_list) == 0:
		resultTweet = "Sorry, can't find tweet with " + query;
	else:
		tweetAuthor = tweets_list[0][0]
		tweetText = tweets_list[0][1]
		resultTweet = "[" + tweetAuthor + "]" + " tweeted: " + tweetText
	return resultTweet;

