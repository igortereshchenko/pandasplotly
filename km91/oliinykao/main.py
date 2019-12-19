import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')


QUERY = """
        SELECT tree_id, legal_status, species, plant_date
        FROM `bigquery-public-data.san_francisco.street_trees`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)
print(df.head(5))


trace3 = go.Scatter(

                    )



trace2 = go.Pie(

                    )

trace1 = go.Bar(
                    x = df['plant_date'].values,
                    y = df['tree_id'].index
)

data = [trace1]

layout1 = dict(
              title = 'trees',
              xaxis= dict(title= 'plant date'),
              yaxis=dict(title='number of trees'),
             )
fig = dict(data = [trace1], layout = layout1)
plot(fig)