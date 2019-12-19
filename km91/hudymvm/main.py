import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')


QUERY = """
        SELECT category, dayofweek, latitude, timestamp
        FROM `bigquery-public-data.san_francisco.sfpd_incidents`
        LIMIT 10
        """

df = bq_assistant.query_to_pandas(QUERY)
print(df.head(5))

category = df['category']
latitude = df['latitude']


trace1 = go.Scatter(
                x = category.index,
                y = latitude.values,
                mode = 'lines'
                    )

day = df['dayofweek']
time = df['timestamp']

data = [trace1]


fig = dict(data = [trace1])
plot(fig)