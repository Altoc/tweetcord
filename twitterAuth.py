import os
from dotenv import load_dotenv
import time
import tweepy
from time import sleep

dotenv_path = 'keys.env'
load_dotenv(dotenv_path)

#load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN_KEY'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth, wait_on_rate_limit=True)
