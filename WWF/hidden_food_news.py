import newspaper


def check_title(news_source):
    for article in news_source.articles:
        if "strange food" or "weird_food" or "travel food" or "disgusting food" in article.title:
            print(article.title)
        else:
            print("None found")


def main():
    cnn_source = newspaper.build('http://www.cnn.com', language='en')
    check_title(cnn_source)

if __name__ == '__main__':
    main()