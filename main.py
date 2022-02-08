#Import Modules
import random
import time
from keep_alive import keep_alive
from Authenticate import get_twitter_api
from Follow_back import Follow_back


#Calling out keep_alive function to get the url to make this bot 24/7.

keep_alive()

#Calling out Follow_back function to make bot follow the users who follow it

Follow_back()

#Fuction to get a random quote from Quotes.txt
def GetQuote():
    Open_quote_file = open('Quotes.txt', encoding="utf8").read().splitlines()
    myQuote =random.choice(Open_quote_file)
    return myQuote #returns the quote


#Function to tweet
def tweet_quote():
    
    Time_interval = 60 * 60 * 1 #Time interval is set to 1 hour(s).

    api = get_twitter_api()

    while True:
        print('Making The quotes ready!')        
        tweet = GetQuote()
        print(tweet)
        if tweet.split():
            api.update_status(status=tweet)#Tweets it
            time.sleep(Time_interval) 


#Calling out main function
if __name__ == "__main__":
    tweet_quote()

#@SidTheMiner
    
    
    






