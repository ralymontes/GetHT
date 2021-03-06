import os
from lib.twitter.clienttwitter import TwitterClient
from lib.config.appconfig import TwitterConfig
import sys


#for arg in sys.argv:
if (len(sys.argv) != 2):
	print("Uso: python app.py [option]")
	exit(0)
option = sys.argv[1]
config_file_path = os.path.join(os.getcwd(), 'config.yml')

twitter_config = TwitterConfig(config_file_path)

twitter_client = TwitterClient(twitter_config.get_property('access_token'), twitter_config.get_property('access_secret'), twitter_config.get_property('consumer_key'), twitter_config.get_property('consumer_secret'), twitter_config.get_property('path'))

if (option == "hashtags" or  option == "users"):
	twitter_client.validateConnectionOption(option)
else:
	print ("Invalid option")
	exit(0)
