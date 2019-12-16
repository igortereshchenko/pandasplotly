import os
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')

QUERY = """
        SELECT `title`, `release_year`, `locations`, `production_company` FROM `bigquery-public-data.san_francisco.film_locations` 
        LIMIT 30
        """

df = bq_assistant.query_to_pandas(QUERY)

g_year_count = df.groupby(['release_year'])['title'].count()
g_prod_count = df.groupby(['production_company'])['title'].count()
g_loc_count = df.groupby(['locations'])['title'].count()

trace1 = go.Scatter(
    x=g_year_count.index,
    y=g_year_count.values,
    mode='lines',
    name='123'
)

trace2 = go.Pie(
    labels=g_loc_count.index,
    values=g_loc_count.values,
)

trace3 = go.Bar(
    x=g_prod_count.index,
    y=g_prod_count.values
)

layout1 = go.Layout(
    title='Кільсість створених фільмів відносно років',
    xaxis=dict(title='Years'),
    yaxis=dict(title='Counts'),
)

layout3 = go.Layout(
    title='Кількість фільмів випущених копманіями',
    xaxis=dict(title='Name of company'),
    yaxis=dict(title='Counts'),
)

fig1 = go.Figure(data=[trace1], layout=layout1)
fig2 = go.Figure(data=[trace2])
fig3 = go.Figure(data=[trace3], layout=layout3)

plot(fig2)
