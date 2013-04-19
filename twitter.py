# -*- coding: utf-8 -*-
import tweepy
import twitter_key
import urllib                                                               
consumer_key = twitter_key.C_KEY
consumer_secret = twitter_key.C_SECRET
access_key = twitter_key.A_KEY
access_secret = twitter_key.A_SECRET

# create OAuth handler                                                      
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)                   
# set access token to OAuth handler                                         
auth.set_access_token(access_key, access_secret)                            
# create API                                                                
api = tweepy.API(auth_handler=auth)                                         
                                                                            
# post kani
#for i in range(10):
#  api.update_status('%d 回目' % i)

# 検索
results = api.search(urllib.quote_plus("foo"))

# 結果を整形
for result in results:
    print result.text # とりあえず表示するだけ
