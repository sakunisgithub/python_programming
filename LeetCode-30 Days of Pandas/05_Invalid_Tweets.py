import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['counts'] = tweets['content'].str.len()
    return tweets.loc[tweets['counts'] > 15, ['tweet_id']]