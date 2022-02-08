#Import Modules
import tweepy

#This Fucntion will authenticate the account and return the api
def get_twitter_api():
    # personal details
    consumer_key = "OuZ2lswZz4US2Fls7mc5jOIqs"
    consumer_secret = "8pJl0wqHHl0lvvETCsfj94OKrQzlNAV2njnmJO5Os9Q2n2Xvdu"
    access_token = "1490221645906456578-DW66eUmwCStgXdZc6Pfizi6ckQb69W"
    access_token_secret = "rZ44X20B6MfRKeuwcw6dGyXdlIh5obBPpQ7U628qRFTcu"
    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


#@SidTheMiner

#Keys

#Api key-OuZ2lswZz4US2Fls7mc5jOIqs

#Api key secret-8pJl0wqHHl0lvvETCsfj94OKrQzlNAV2njnmJO5Os9Q2n2Xvdu



#bearer key-AAAAAAAAAAAAAAAAAAAAAJi0YwEAAAAAC1dKXukYFS8D1bb2GjJnF%2FWDb2A%3DCLbqNKm2saowL1ONxgiIznubf02vV2LQS8Ujbc4gcMkOms7JKl



#access key-1490221645906456578-DW66eUmwCStgXdZc6Pfizi6ckQb69W

#access key sectret-rZ44X20B6MfRKeuwcw6dGyXdlIh5obBPpQ7U628qRFTcu




#client id-Y20wb1RVMGt4N1FlQXNhSURrQ2k6MTpjaQ
#Client id secret-YzTXWhNAcw1iQrkhwTXA4rZgxBX-KpOaF7JnCfWA2VjciZKEKG