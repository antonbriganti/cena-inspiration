import twint

def get_tweets():
    tweets = []

    search_config = twint.Config()

    search_config.Username = 'JohnCena'
    search_config.Limit = 20
    search_config.Hide_output = True
    search_config.Store_object = True
    search_config.Store_object_tweets_list = tweets

    twint.run.Search(search_config)

    return tweets

def filter_tweets(tweets):
    return [tweet.tweet for tweet in tweets if "#" not in tweet.tweet]


if __name__ == "__main__":
    cena_tweets = get_tweets()
    filtered_cena_tweets = filter_tweets(cena_tweets)
    print(filtered_cena_tweets)