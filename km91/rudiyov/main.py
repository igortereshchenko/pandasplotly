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
values_act = df['call_date'].value_counts().reset_index().sort_values(by='index')
values_city = df['city'].value_counts().reset_index().sort_values(by='index')

trace1 = go.Scatter(
    x=values_act['index'],
    y=values_act['call_date'],
    mode="lines+markers",
    name="Активність"
)

trace2 = go.Pie(
    labels=values_city['index'],
    values=values_city['city']
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
layout_scatter = dict(
    xaxis=dict(title='Дата'),
    yaxis=dict(title='кількість викликів'),
    title='Активність'

)
fig_bar = dict(data=[trace3], layout=layout_bar)
fig_scatter = dict(data=[trace1], layout=layout_scatter)
fig_pie = dict(data=[trace3])
plot(fig_pie)
