import tweepy
from tweepy import API
from keys import *
import json
import preprocessor as p
import argparse

parser = argparse.ArgumentParser(description='get tweet')

parser.add_argument("--count",metavar='get count', default=50,type=int,help='number of tweets to fetch')

def main():

	global args;

	args = parser.parse_args()

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	all_tweets = []
	public_tweets = api.home_timeline(tweet_mode="extended",count = args.count)
	i = 0
	with open('saved_tweets.txt', 'w') as f:
	    for tweet in public_tweets:
	        is_retweet = tweet.full_text.lower().startswith("rt @")    
	        if(is_retweet):
	            all_tweets.append(str(tweet.retweeted_status.full_text).replace("\n"," ").replace("'"," ").replace('"',' '))#p.clean(tweet.retweeted_status.full_text))#.replace("\n"," ").replace("\""," ").replace("\'"," "))
	            print(tweet.retweeted_status.full_text.replace("\n"," ").replace("'"," ").replace('"',' ')) #p.clean(tweet.retweeted_status.full_text.replace("\n"," ")))
	#             f.write(str(i))
	#             f.write("  \"%s\", " % str(tweet.retweeted_status.full_text).replace("\n"," ").replace("\""," ").replace("\'"," "))
	        else:
	            all_tweets.append(str(tweet.full_text).replace("\n"," ").replace("'"," ").replace('"',' '))#p.clean(tweet.full_text))#.replace("\n"," "))
	            print(tweet.full_text.replace("\n"," ").replace("'"," ").replace('"',' '))#p.clean(tweet.full_text.replace("\n"," ")))
	#             f.write(str(i))
	#             f.write("  \"%s\", " % str(tweet.full_text).replace("\n"," "))
	#         f.write("\n\n")
	        print("\n")
	        print("-----Next tweet-----")
	        print("\n")
	        i = i+1
	        
	# Serializing json 
	json_object = json.dumps(all_tweets)

	# print("data =",json_object)
	# Writing to sample.json
	with open("saved_tweets.json", "w") as outfile:
	    outfile.write("data = '")
	    outfile.write(json_object)
	    outfile.write("';")

if __name__ == '__main__':
	main()