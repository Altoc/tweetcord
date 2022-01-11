# tweetcord
 
 If you just want to add the original, world famous Twitter Feller, use this link:
     https://discord.com/api/oauth2/authorize?client_id=719666409134882916&permissions=51200&scope=bot
 
Tweetcord is an opensource discord bot that searches twitter for any activity relating to the queried phrase. Here is an example of what tweetcord does:

![twitter feller demo](https://user-images.githubusercontent.com/37989193/148867518-5452b4fc-68d0-4ed2-97f7-0fbb2b85a982.PNG)


Here are some modifiers that tweetcord is capable of. These are mostly just wrapped around functionality of Tweepy.
     ["ian is cool"] will only search for the exact phrase
     [love OR hate] will search either love or hate (or both)
     [beer -root] will search beer, but not root
     [#insectulon] will search for tweets with this hashtag
     [from:NASA] will search for tweets from the account NASA
     [to:NASA] will search for tweets directed at NASA
     [@NASA] will search for tweets that mention NASA account
     [politics filter:safe] with 'politics' but with sensitive tweets removed
     [puppy filter:media] puppy tweets with an image or video
     [puppy -filter:retweets] puppy tweets, with retweets filtered out
     [puppy filter:periscope] puppy tweets with a persicope video URL
     [puppy filter:vine] puppy tweets with a Vine
     [puppy filter:links] puppy tweet with a URL link
     [puppy url:amazon] puppy tweet with word 'amazon' in a link
     [movie -scary :)] a tweet with 'movie', w/o 'scary', and with a positive attitude
     [movie :(] a tweet with 'movie', and a negative attitude
     [movie ?] a tweet with 'movie', and asking a question
