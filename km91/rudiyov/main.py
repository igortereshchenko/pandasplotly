import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('san_francisco', 'bigquery-public-data')

QUERY = """
        SELECT `unit_id`,`call_type`,`call_date`,`city` FROM `bigquery-public-data.san_francisco.sffd_service_calls`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)

values = df['call_type'].value_counts().reset_index().sort_values(by='index')

trace1 = go.Scatter(

)

trace2 = go.Pie(

)

trace3 = go.Bar(
    x=values['index'],
    y=values['call_type']
)

data = [trace1]

layout_bar = dict(
    title='Type',
    xaxis=dict(title='types'),
    yaxis=dict(title='counts'),
)
fig_bar = dict(data=[trace3], layout=layout_bar)
plot(fig_bar)
