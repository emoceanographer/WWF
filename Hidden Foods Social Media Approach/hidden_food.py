import tweepy
import csv
import pandas as pd
import preprocessor as tc


def build_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def write_to_pandas(api, queries, file_name):
    csv_file = open(file_name, 'w')
    csv_writer = csv.writer(csv_file)
    tweets_list = []
    locations_list = []
    for tweet in tweepy.Cursor(api.search, q=queries, count=30000,
                               lang="en",
                               since="2008-01-01").items():
        clean_text = tc.clean(tweet.text)
        clean_location = tc.clean(tweet.user.location)
        tweets_list.append(clean_text)
        locations_list.append(clean_location)
    tweet_frame = pd.DataFrame(
        {'tweets': tweets_list,
         'location': locations_list,
         })
    tweet_frame.to_pickle("tweet_frame.df")
    tweet_frame.to_csv(file_name)


# def panda_clean(file_name):
#     hidden_food_data = pd.read_csv(file_name, names=["tweets", "location"], encoding="utf8")
#     hidden_food_data['tweets'].replace(regex=True, inplace=True, to_replace=r"[\xef\x\xf]", value=r'')
#     hidden_food_data['location'].replace(regex=True, inplace=True, to_replace=r"[\xef\x\xf]", value=r'')
#     #print(hidden_food_data.head(30))


def main():
    api = build_api()
    tourist_queries = '#strangefood OR #unusualfood ' \
                      'OR #disgustingfood OR #weirdfood ' \
                      'OR \"weird food\" OR \"strange food\" ' \
                      'OR \"disgusting food\" OR \"unusual food\" ' \
                      'OR \"travel food\"'
    write_to_pandas(api, tourist_queries, "hidden_food_tourists.csv")

    local_queries = '#foraging OR #forage ' \
                    'OR #foragefood OR #foragingfood ' \
                    'OR #wildfood OR #wildlifefood ' \
                    'OR #foragewildfood OR #cookwildlife ' \
                    'OR #ancientfood OR #foragingfood ' \
                    'OR #hunt OR #bushmeat ' \
                    'OR \"forage\" OR  \"foraging\"' \
                    'OR \"wild animal for food\" OR \"cook wild animal\" ' \
                    'OR \"eat wildlife\" OR \"eat wild animal\" ' \
                    'OR \"wild animal market\" OR \"bizarre food\"' \
                    'OR \"ancient recipe\" OR \"bushmeat\" -filter:retweets'
    write_to_pandas(api, local_queries, "hidden_food_tweets_local.csv")


if __name__ == '__main__':
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    tc.set_options(tc.OPT.URL, tc.OPT.EMOJI, tc.OPT.MENTION, tc.OPT.EMOJI)
    main()
