from instabot import Bot
from config import config;

bot = Bot()
bot.login(username=config.username, password=config.password)
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_info(user_id)
print(user_info['biography'])


#https://instagrambot.github.io/docs/en/For_developers.html#Quickstart/////