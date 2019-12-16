import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper("bigquery-public-data", "san_francisco")


QUERY = """
        SELECT `trip_id`, `duration_sec`, `start_station_name`, `subscriber_type` 
        FROM `bigquery-public-data.san_francisco.bikeshare_trips`
        LIMIT 15
        """


df = bq_assistant.query_to_pandas(QUERY)


trace1 = go.Scatter(
    x=df.trip_id.index,
    y=df.duration_sec.values,
    mode="lines",
    name="trip duration by trip")
layoutScatter = dict(
    title="placeholder",
    xaxis=dict(
        title="tripnumber"
    ),
    yaxis=dict(
        title="tripduration"
    )
)
tracescatter=dict(data=[trace1],layout=layoutScatter)
plot(tracescatter)

#numberofcustomers = df.groupby(["subscriber_type"])["trip_id"].count()


#mypiegraph = go.Figure(
data=[go.Pie(labels=numberofcustomers.index, values=numberofcustomers.values)]
)
#plot(mypiegraph)




trace3 = go.Bar(
x=df.trip_id.index,
y=df.duration_sec.values)
layout = go.Layout(
    title='bike rides',
    xaxis=dict(title='trip_id'),
    yaxis=dict(title='trip_duration'),
)
mybargraph = go.Figure(data=[trace3], layout=layout)
plot(mybargraph)
