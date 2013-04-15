# -*- coding: utf-8 -*-
import tweepy
import twitter_key                                                               

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
api.update_status("test")   
