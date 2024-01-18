from selenium import webdriver
from internet_speed import InternetSpeedTwitterBot

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(edge_options)

bot = InternetSpeedTwitterBot(driver)
bot.post_twitter_message()

