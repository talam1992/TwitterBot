__author__ = 'Timothy Lam'

from twython import Twython

from auth import (
    conusmer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython (
    conusmer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "#Tweeting using #Twitterbot with #Python!"
twitter.update_status(status=message)
print("Tweeted: {}" .format(message))

