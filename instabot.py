from instabot import Bot
from config import config;
import pandas as pd;




class InstaBot:
    

    
    
    def __init__(self):
        self.bot = Bot();
        self.bot.login(username = config["username"], password = config["password"])
        self.users_followed = [ ]
        self.user_follower_list = [ ]
    
    #make csv of people following a user from their username
    #and internal list inside bot of people followinf a user
    def get_followers_list(self, username, csv = True):
        bot = self.bot
        
        
        #get user_id from username
        user_id  = bot.get_user_id_from_username(username)
        
        #get list of users followers
        user_followers = bot.get_user_followers(user_id)
        
        #put list into self for later usage
        self.user_follower_list = user_followers
        
        #if csv if false only get followers and don't return csv
        if(csv):
            #turn userlist into csv
              user_csv = pd.DataFrame(user_followers)
              user_csv.to_csv(f'{username}.csv')
              
        
        
 
    #given a users followers csv, follow x amount of them
    #and internal list inside of bot of who you followd
    def follow_from_csv(self, user_csv, count):
        #input csv file name
         user_csv = user_csv;
         
         #turn csv into a dataframe
         df = pd.DataFrame(user_csv)
         
         #turn csv into list
         df_list = df.values.tolist()
         
         #follow count amount of people from list
         for x in count:
             self.bot.follow(df_list[x])
             #add user to users followed list
             self.users_followed.append(df_list(x))
    
  
    #follow from internal list
    def internal_follow(self, count):
        follow_list = self.user_follower_list
         #follow count amount of people from list
        for x in count:
            self.bot.follow(follow_list[x])
            #add user to users followed list
            self.users_followed.append(follow_list(x))        
        
    #like x amount of users pictures
    #internal list of followed users needs to be created
    def like_followed_user_media(self):
        if self.users_followed == None:
            return 'no internal list'
        followed_users = self.users_followed;
        #get user photos
        #recursively like them 
       
         
         
        




