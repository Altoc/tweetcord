import twitterAuth
import twitterLookup
import tweepy

api = twitterAuth.api;

query = input("Query: ");

result = twitterLookup.twitterLookup(query, 1)
print(result)


