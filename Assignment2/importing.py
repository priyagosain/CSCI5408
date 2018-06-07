import csv
import locale


import rpp as rpp
import tweepy
import time
import json

from tweepy import API

consumer_key = "2FVQutC6ddbRB3JZ59agcPhp7"
consumer_secret = "j1ABuhLcuYNM1IjkhHnNo2cZoeC2oo8rfeoLhcxaSorsULBFmh"
access_key = "1000034486401282054-J7Vu0QOZdOQu9fChHtn4tJi7qmYz18"
access_secret = "Z9oDvkMxrhWSGAD0JiOK5yA6SBneZNJIRQDBTXm8k0jT1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def get_profile(screen_name):
    api = tweepy.API(auth)
    try:
        # https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except tweepy.error.TweepError as e:
        user_profile = json.loads(e.response.text)

    return user_profile


def get_trends(location_id):
    api = tweepy.API(auth)
    try:
        # https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place.html
        trends = api.trends_place(location_id)
    except tweepy.error.TweepError as e:
        trends = json.loads(e.response.text)
        return trends



def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]

    return tweets


tw = get_tweets("#CampDay")

queries = ["#CampDay", "\"Canada\"", "@Windows", "#TimHortons"]
with open('tweets.csv', 'w', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    lang="en"
    writer.writerow(['id', 'user', 'created_at', 'text'])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            writer.writerow([tweet.id_str, tweet.user.screen_name, tweet.created_at, tweet.text])
