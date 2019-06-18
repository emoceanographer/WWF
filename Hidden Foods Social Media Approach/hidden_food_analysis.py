import pandas as pd
import nltk
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


# %matplotlib inline

# Enable logging for gensim - optional

def pre_processing():
    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
    tweet_frame['tweet_tokens'] = tweet_frame.apply(lambda row: tokenization(row["tweets"]), axis=1)


def tokenization(tweets):
    return gensim.utils.simple_preprocess(str(tweets), deacc=True)


if __name__ == '__main__':
    tweet_frame = pd.read_pickle("tweet_frame.df")
    print(tweet_frame.shape[0])
    pre_processing()
    pprint(tweet_frame.head(5))
    tweet_frame.to_csv("tweet_data.csv")
