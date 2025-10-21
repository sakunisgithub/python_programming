import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    a = (views['author_id'] == views['viewer_id'])
    ids = np.sort(views.loc[a, 'author_id'].unique())
    return pd.DataFrame({'id' : ids})