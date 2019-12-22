import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')

QUERY = """
        SELECT  station_id, docks_available, bikes_available, time
        FROM `bigquery-public-data.san_francisco.bikeshare_status`
        LIMIT 10
        """
df = bq_assistant.query_to_pandas(QUERY)
id_bike_df = df[df['station_id']==90]
bike_id_groupby = id_bike_df.groupby(['docks_available'])['bikes_available'].sum()

trace1 = go.Scatter(
    x=bike_id_groupby.index,
    y=bike_id_groupby.values,
    mode = "lines",
    name = "request_status")
trace3 = go.Bar(x=['87', '90', '91'],
                y=[1, 8, 2])

layout_1 = dict(
              title = 'bikeshare_status',
              xaxis= dict(title= 'station_id'),
              yaxis=dict(title='bikes_available'),
             )
layout_2 = dict(
              title = 'status_of_request',
              xaxis= dict(title= 'station_id'),
              yaxis=dict(title='docks_available'),
             )

fig_1 = dict(data = [trace1], layout = layout_1)
plot(fig_1)
fig_2 = dict(data = [trace3], layout = layout_2)
plot(fig_2)