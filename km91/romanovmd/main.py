import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')


QUERY = """
        SELECT  station_id, bikes_available, docks_available, time
        FROM `bigquery-public-data.san_francisco.bikeshare_status`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

id_bike_df = df[df['station_id']==90];
bike_id_groupby = id_bike_df.groupby(['bikes_available'])['docks_available'].sum()

trace1 = go.Scatter(
    x=bike_id_groupby.index,
    y=bike_id_groupby.values,
    mode = "lines",
    name = "status_of_request",
                    )



trace2 = go.Pie(

                    )

trace3 = go.Bar(x=['87', '90', '91'],
                y=[0, 7, 3]
)

data = [trace1]

layout = dict(
              title = 'bikeshare_status',
              xaxis= dict(title= 'station_id'),
              yaxis=dict(title='bikes_available'),
             )
layout_2 = dict(
              title = 'status_of_request',
              xaxis= dict(title= 'station_id'),
              yaxis=dict(title='docks_available'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)
fig_2 = dict(data = [trace3], layout = layout)
plot(fig_2)