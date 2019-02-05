import tweepy
import csv
import pandas as pd


def build_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def write_to_csv(api, queries):
    csv_file = open('hidden_food.csv', 'w')
    csv_writer = csv.writer(csv_file)
    for tweet in tweepy.Cursor(api.search, q=queries, count=30000,
                               lang="en",
                               since="2010-01-01").items():
        print(tweet.created_at, tweet.text)
        csv_writer.writerow([tweet.text.encode('utf-8'), tweet.user.location.encode('utf8')])


def panda_clean():
    hidden_food_data = pd.read_csv('hidden_food.csv', encoding='utf-8')
    print(hidden_food_data.head(30))


def main():
    # api = build_api()
    # queries = '#strangefood  OR  #unusualfood OR #disgustingfood OR #weirdfood OR #food'
    # write_to_csv(api, queries)
    panda_clean()


if __name__ == '__main__':
    consumer_key = "0Q5kFRey7Wzj5Zp1hQFgdf1cp"
    consumer_secret = "6f70qpDxWGy4la7RbSsOuVrGAfLXdxq7wYJEcsH6AiJvKT5pum"
    access_token = "1090257492137906176-6x0WMlHFuxsILjGfbvwnRbcuz8TqIf"
    access_token_secret = "5aKJzqTnProSn9iTOjZdiCxfIGjZn4MJYbCVrdzHN0IBT"
    main()
