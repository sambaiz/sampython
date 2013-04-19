from oauth2 import Client, Token, Consumer 
import twitter_key

consumer_key = twitter_key.C_KEY
consumer_secret = twitter_key.C_SECRET


def split_parameter(parameters):
    result_list = [tuple(parameter.split('='))
                   for parameter in parameters.split('&')]
    return dict(result_list)

consumer = Consumer(consumer_key, consumer_secret)
client = Client(consumer, None)
result = client.request('http://api.twitter.com/oauth/request_token',
                        'GET')
request_token_map = split_parameter(result[1])
request_token = Token(request_token_map['oauth_token'],
                      request_token_map['oauth_token_secret'])

print 'Please access "http://api.twitter.com/oauth/authorize?oauth_token='+request_token.key+'".'
pin = raw_input('PIN:')
request_token.set_verifier(pin)

client.token = request_token
result = client.request('http://api.twitter.com/oauth/access_token',
                        'POST')

access_token_map = split_parameter(result[1])
print result[1]
print 'User key: '+access_token_map['oauth_token']
print 'User secret: '+access_token_map['oauth_token_secret']
raw_input('Push any key to quit.')

