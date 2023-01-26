import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))
print(ad_clicks.groupby("utm_source").user_id.count().reset_index())
ad_clicks["is_click"] =  ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()

clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()


clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']
