#prueba en Python con extraccion de datos. Prueba para realizar experimento "Social". Caso: Video UTP

import tweepy

consumer_key= "8MUlhLXlsggAFYC1VyzlaaD5q"
consumer__key_secret="ozLRT6AqbV1EJG4esvpxpENVgXb7LqABT3o7pO8vvG9ytRXnjo"
access_token="1129264063064805376-eQpp7FafDtob4eiWuaUsICDSiFeJUW"
access_token_secret="sjmPulB64Cs6R85o0nC1QMKATMPEXTrmQeVunsfwLOeJ0"

autenticar= tweepy.OAuthHandler(consumer_key,consumer__key_secret)
autenticar.set_access_token(access_token,access_token_secret)

api = tweepy.API(autenticar)

#----------------------------------------------------------------------

#usuario de twitter
username = "elonmusk"

# número de tweets

tweetCount = 20

resultado = api.user_timeline(id=username, count=tweetCount)

print("username" + "     "+ "tweet")
for tweet in resultado:
    print(username + "     "+ tweet.text)