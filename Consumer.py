from kafka import KafkaConsumer
import Properties
import sqlite3
import json

topic_name = Properties.topic_name

consumer = KafkaConsumer(
    topic_name,
     bootstrap_servers=Properties.bootstrap_servers,
     auto_offset_reset=Properties.auto_offset_reset,
     enable_auto_commit=Properties.enable_auto_commit,
     auto_commit_interval_ms = Properties.auto_commit_interval_ms,
     fetch_max_bytes = Properties.fetch_max_bytes,
     max_poll_records =Properties.max_poll_records,

     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

conn = sqlite3.connect("Twitter.db")
c= conn.cursor()

for message in consumer:
 tweets = json.loads(json.dumps(message.value))
 if tweets['retweeted']== True:
  continue
 text = tweets['text']
 if text.find('singer') >=0:
  created_at = tweets['created_at']
  favorite_count = tweets['favorite_count']
  favorited = tweets['favorited']
  filter_level = tweets['filter_level']
  lang = tweets['lang']
  retweet_count = tweets['retweet_count']
  retweeted = tweets['retweeted']
  source = tweets['source']
  truncated = tweets['truncated']
  user_created_at = tweets['user']['created_at']
  user_followers_count = tweets['user']['followers_count']
  user_location = tweets['user']['location']
  user_lang = tweets['user']['lang']
  user_name = tweets['user']['name']
  user_screen_name = tweets['user']['screen_name']
  user_time_zone = tweets['user']['time_zone']
  user_utc_offset = tweets['user']['utc_offset']
  user_friends_count = tweets['user']['friends_count']
  c.execute('''INSERT INTO tweets(created_at,favorite_count,favorited,filter_level,lang,retweet_count,retweeted,source,text,truncated,user_created_at,
  user_followers_count,user_location,user_lang,user_name,user_screen_name,user_time_zone,user_utc_offset,user_friends_count) 
  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(created_at,favorite_count,favorited,filter_level,lang,retweet_count,retweeted,source,text,truncated,user_created_at,
  user_followers_count,user_location,user_lang,user_name,user_screen_name,user_time_zone,user_utc_offset,user_friends_count))
  conn.commit()
  # print(tweets)