from google_play_scraper import search, reviews
import pandas as pd


def search_app(term):
    # result = search(term, fullDetail=True, throttle=10, num=250)
    result = search(
    term,
    lang="en",  # defaults to 'en'
    country="us",  # defaults to 'us'
    n_hits=35  # defaults to 30 (= Google's maximum)
    )

    data = pd.DataFrame(result)
    # ['appId', 'icon', 'screenshots', 'title', 'score', 'genre', 'price',
    #        'free', 'currency', 'video', 'videoImage', 'description',
    #        'descriptionHTML', 'developer', 'installs']

    return data


def search_reviews(app_id, count=100):
    
    review_batch = reviews(
        app_id,
        lang='en',
        country='us',
        count=count,
    )
    
    # return (app_id, [review['content'] for review in review_batch])
    return [review['content'] for review in review_batch[0] if review['content'] is not None]
            

    