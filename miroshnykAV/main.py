
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','san_francisco')


QUERY = """
        SELECT species, site_order, plant_date ,tree_id
        FROM `bigquery-public-data.san_francisco.street_trees`
        LIMIT 150
        """


df = bq_assistant.query_to_pandas(QUERY)


bar=go.Bar(x=df['species'],y=df["site_order"])
layout=go.Layout(title='species',xaxis=dict(title="species"),yaxis=dict(title="site_order"),)
fig=go.Figure(data=[bar],layout=layout)
plot(fig)

labels = df['species']
values = df["site_order"]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
plot(fig)