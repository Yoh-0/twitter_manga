import tweepy
# from html.parser import HTMLParser

#Twitterの認証
consumer_key = 'VeaCyexExiyCJNuxG5CKLfMB9'
consumer_secret = 'nFCaAdsbcE4MvQnkvJN3SMDJt3WEHSecNOuI3AFTNgOmwj2LJh'
access_token = '921676480576290816-sGFjrl94Fxj6eTQMdHSV3PoK5jAfTsa'
access_token_secret = 'HFXx7fWXVweuIg9hDvqywObyKvmo2KidsLLRASgLahG0t'


auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
   def searchtweet(keyword):
      tweets = api.search(q=keyword, count=3)
      return tweets

   keyword = 'マンガ'
   print(tweet.text)

