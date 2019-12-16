import pandas as pd
import numpy as pn
import plotly.graph_objs as go
import os
from plotly.offline import plot

from bq_helper import BigQueryHelper
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')


QUERY = """
        SELECT unique_key, descript, dayofweek, category FROM `bigquery-public-data.san_francisco.sfpd_incidents`
        LIMIT 100
        """
df = bq_assistant.query_to_pandas(QUERY)
print(df.head(4))

trace1 = go.Scatter(
                    x = df['unique_key'].index,
                    y = df['category'],
                    mode = "lines",
                    name = "category",
                    )
layout = dict(title = '',
              xaxis= dict(title= 'unique_key'),
              yaxis=dict(title='category'),
             )
fig = dict(data=[trace1],layout=layout)

plot(fig)

trace2 = go.Scatter(
                    x = df['description'].index,
                    y = df['dayofweek'].values,
                    mode = "lines+markers",
                    name = "male"
                    )

data = [trace1, trace2]

layout = dict(title = 'accidents',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fog = dict(data = [trace1, trace2], layout = layout)
plot(fog)
