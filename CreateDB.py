import sqlite3
conn = sqlite3.connect("Twitter.db")
c= conn.cursor()
tb_create=""" CREATE TABLE tweets
(created_at,favorite_count,favorited,filter_level,lang,retweet_count,retweeted,source,text,truncated,user_created_at,
user_followers_count,user_location,user_lang,user_name,user_screen_name,user_time_zone,user_utc_offset,user_friends_count)"""
c.execute(tb_create)
conn.commit()