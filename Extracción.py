#prueba en Python con extraccion de datos.

#Libreria Tweepy de python permite utilizar las apis de Twitter para la mineria de datos
import tweepy

#La consumer key(Api Key), consumer key secret, access token y access token secret se consiguen cuando creas un aplicacion en twitter
consumer_key= "XXXXXXXXXXXXXXXXX"
consumer__key_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#estas llaves y tokens se utilizan para autenticar al usuario por motivos de seguridad
autenticar= tweepy.OAuthHandler(consumer_key,consumer__key_secret)
autenticar.set_access_token(access_token,access_token_secret)

#se crea un variable llamada api que almecena la autenticacion 
api = tweepy.API(autenticar)

#----------------------------------------------------------------------

#usuario de twitter
username = "elonmusk"

# número de tweets
tweetCount = 20

#La funcion timeline nos permite ver los tweets del usuario elegido
resultado = api.user_timeline(id=username, count=tweetCount)

print("username" + "     "+ "tweet")

for tweet in resultado:
    print(username + "     "+ tweet.text)
