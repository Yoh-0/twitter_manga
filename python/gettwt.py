import tweepy

#Twitterの認証
consumer_key = 'VeaCyexExiyCJNuxG5CKLfMB9'
consumer_secret = 'nFCaAdsbcE4MvQnkvJN3SMDJt3WEHSecNOuI3AFTNgOmwj2LJh'
access_token = '921676480576290816-sGFjrl94Fxj6eTQMdHSV3PoK5jAfTsa'
access_token_secret = 'HFXx7fWXVweuIg9hDvqywObyKvmo2KidsLLRASgLahG0t'

# #Twitterの認証
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# #　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
# api=tweepy.API(auth,wait_on_rate_limit=True)

# 検索条件の設定
#min_favesはいいねの件数が最低200件以上のツイートのみを取得する.変更可能
#*****に検索キーワードを入力する

# search_word = 'マンガ, 漫画 min_faves:200'
# #何件のツイートを取得するか
# item_number = 10

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)