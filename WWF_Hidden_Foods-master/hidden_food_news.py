import newspaper as ns
import googlesearch as google
import time


# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types

def check_title(news_source):
    for article in news_source.articles:
        article.download()
        article.parse()
        if "strange food" or "weird_food" or "travel food" or "disgusting food" in article.title.lower():
            print(article.title)
        else:
            print("None found")


def check_title_grab_url():
    for url in google.search("weird travel food", stop=33):
        try:
            article = ns.Article(url)
            article.download()
            article.parse()
            print(article.title)
            time.sleep(0.01)
        except:
            continue


def main():
    # cnn_source = ns.build('http://cnn.com', language='en')
    # check_title(cnn_source)
    check_title_grab_url()



if __name__ == '__main__':
    main()
