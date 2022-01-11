import os
import discord
import discordAuth
import twitterAuth
import twitterLookup

client = discordAuth.client

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content == '!help':
		helpResult = """Here are some cool modifiers you can use:\n 
			     [\"ian is cool\"] will only search for the exact phrase\n 
			     [love OR hate] will search either love or hate (or both)\n
			     [beer -root] will search beer, but not root\n
			     [#insectulon] will search for tweets with this hashtag\n
			     [from:NASA] will search for tweets from the account NASA\n
			     [to:NASA] will search for tweets directed at NASA\n
			     [@NASA] will search for tweets that mention NASA account\n
			     [politics filter:safe] with 'politics' but with sensitive tweets removed\n
			     [puppy filter:media] puppy tweets with an image or video\n
			     [puppy -filter:retweets] puppy tweets, with retweets filtered out\n 
			     [puppy filter:periscope] puppy tweets with a persicope video URL\n
			     [puppy filter:vine] puppy tweets with a Vine\n
			     [puppy filter:links] puppy tweet with a URL link\n
			     [puppy url:amazon] puppy tweet with word 'amazon' in a link\n
			     [movie -scary :)] a tweet with 'movie', w/o 'scary', and with a positive attitude\n
			     [movie :(] a tweet with 'movie', and a negative attitude\n
			     [movie ?] a tweet with 'movie', and asking a question"""
		await message.channel.send(helpResult)
	if message.content[0:4] == '!ian':
		response = message.content[5:]
		lookupResult = twitterLookup.twitterLookup(response, 1)
		await message.channel.send(lookupResult)

client.run(discordAuth.TOKEN)
