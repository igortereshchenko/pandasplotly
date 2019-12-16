import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import numpy as np
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','san_francisco')

QUERY = """
        SELECT tree_id, legal_status, plant_date, permit_notes  FROM `bigquery-public-data.san_francisco.street_trees`
        LIMIT 10
        """

df = bq_assistant.query_to_pandas(QUERY)


trace1 = go.Scatter(
                    x = df['tree_id'].index,
                    y = df['legal_status'].values,
                    mode = "lines",
                    name = "female",
                    )


data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)