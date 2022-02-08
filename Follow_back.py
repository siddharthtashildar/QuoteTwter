#Import Modules
from threading import Thread
from Authenticate import get_twitter_api


#This function will follow back the user who follows the bot
def FollowBack_process():
    api = get_twitter_api()
    followers = api.get_follower_ids()
    print("Followers", len(followers))
    friends = api.get_friend_ids()
    print("You follow:", len(friends))
    for follower in followers:
        if follower not in friends:
            api.create_friendship(user_id=follower)

#Thread
def Follow_back():
    t2 = Thread(target=FollowBack_process)
    t2.start()

#@SidTheMiner