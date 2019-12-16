import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')



QUERY = """
        SELECT * FROM `bigquery-public-data.san_francisco.bikeshare_status`
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df.head(10))
trace1 = go.Scatter(

                    )



trace2 = go.Pie(

                    )

trace3 = go.Bar(x = ['station_id'],
                y = ['time']

)

data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)


