# -*- coding: utf-8 -*-
import tweepy
import twitter_key
import urllib                                                               
import random

class Twitter:
  def __init__(self):
    consumer_key = twitter_key.C_KEY
    consumer_secret = twitter_key.C_SECRET
    access_key = twitter_key.A_KEY
    access_secret = twitter_key.A_SECRET
    # create OAuth handler                                                      
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)                   
    # set access token to OAuth handler                                         
    auth.set_access_token(access_key, access_secret)                            
    # create API                                                                
    self.api = tweepy.API(auth_handler=auth)                                         

  def random_select(self, num):
    strs=[]
    for p in tweepy.Cursor(self.api.user_timeline,since_id=10000).items(num):
      strs.append(unicode(p.text))

    return strs[int(random.random()*num)]  
