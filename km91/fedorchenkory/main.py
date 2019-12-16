import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')



QUERY = """
        SELECT * FROM `bigquery-public-data.san_francisco.bikeshare_status`
        LIMIT 11
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df.head(10))
print(df.index)
trace1 = go.Scatter(x = df.index,
                    y = df.values,
                    mode = 'lines',
                    name = 'dd'

                    )



trace2 = go.Pie(

                    )

trace3 = go.Bar(x = ['docks_avaliable'],
                y = ['bikes_avaliable']

)

data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)


