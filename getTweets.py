#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
import csv
import time
from config import CONFIG

# 各種ツイッターのキーをセット
CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

#FLASKのキーの設定
SECRET_KEY = CONFIG["SECRET_KEY"]

#Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth)

#ツイート取得
tweet_data = []

for tweet in tweepy.Cursor(api.user_timeline,screen_name = "never_be_a_pm",exclude_replies = True).items():
	if not tweet.retweeted: #RT入れると他人のRT入っちゃうので除外
		try:  	
		    tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])
		    print(tweet_data)
		except Exception as e: #rate limit到達するとエラーが起こるのでキャッチする
			time.sleep(60 * 15) # 15分で解決するらしいよ

#csv出力
with open('today.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
pass