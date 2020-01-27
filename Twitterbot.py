import tweepy
from config import config

    
#https://tweepy.readthedocs.io/en/latest/getting_started.html

class TwitterBot:
    def __init__(self):
        self.auth  = tweepy.OAuthHandler(config["consumerKey"], config["consumerSecret"]);
        self.auth.set_access_token(config["accessToken"], config["accessSecret"]);
        self.api = tweepy.API(self.auth);
        self.users_followed = []
        self.users_followers = []
        
    #print x number of tweetss
    def timelineTweets(self, count):
        timeline = self.api.home_timeline()
        if count == None:
            return 'please provide a numerical argugment for count'
        
        x = 0
        for tweet in timeline:
            if x == count:
                 print(tweet)
            x = x + 1
            
    #follow users that retweeted a tweet   
    def follow_retweets(self, tweet_id, count =0):
        #get user account id's
        users_retweeted = self.api.retweeters(tweet_id)
        #follow x amount of them
        x = 0 
        for x in count:
            self.api.create_friendship(users_retweeted[x])
            self.users_followed.append(users_retweeted[x])
    
            
         
         

bot = TwitterBot()