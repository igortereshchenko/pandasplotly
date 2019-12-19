import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"
import numpy as np
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-date','san-francisco')

QUERY = """
        SELECT unique_key, created_date, closed_date, status FROM `bigquery-public-date.san_francisco.311_service_request`
        LIMIT 10
        """

df = bq_assistant.query_to_pandas(QUERY)

trace1 = go.Scatter(
                    x = df['unique_key'].index,
                    y = df['created_date'].index,
                    made = "lines",
                    mode = "female"
                    )
data = [trace1]


trace2 = go.Pie(
    x=df['unique_key'].index,
    y=df['created_date'].index,
    made="lines",
    mode="female"
                    )
data = [trace2]
trace3 = go.Bar(
    x=df['unique_key'].index,
    y=df['created_date'].index,
    made="lines",
    mode="female"
                    )

data = [trace3]

layout = dict(
              title = '',
              xaxis = dict(title= ''),
              yaxis = dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)