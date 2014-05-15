import tweepy, json

with open('secret.json') as data_file:    
    data = json.load(data_file)


username = data["twitter"]["username"]
consumer_key = data["twitter"]["consumer_key"]
consumer_secret = data["twitter"]["consumer_secret"]

access_token = data["twitter"]["access_token"]
access_token_secret = data["twitter"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user(username)

print user.screen_name
print user.followers_count
print "\n"

followers_ids = api.followers_ids(username)
following_ids = api.friends_ids(username)

difference = list(set(following_ids) - set(followers_ids))

for unfollower_id in difference:
	unfollower = api.get_user(unfollower_id)
	print unfollower.screen_name
