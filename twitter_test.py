# -*- coding: utf-8 -*-
import tweepy
import twitter_key
import urllib                                                               
import random
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
#query = u"foo" # クエリ
#results = api.search(urllib.quote_plus(query.encode('utf-8')))

# 結果を整形
#for result in results:
#    print result.text # とりあえず表示するだけ

tweet_num = 100
strs=[]
for p in tweepy.Cursor(api.user_timeline,since_id=10000).items(tweet_num):
     strs.append(unicode(p.text))

print strs[int(random.random()*tweet_num)]
