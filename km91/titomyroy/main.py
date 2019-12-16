import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
# import plotly.graph_objs as go
# from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'san_francisco')

QUERY = """

        SELECT call_number, unit_id, call_type, battalion FROM `bigquery-public-data.san_francisco.sffd_service_calls`

        LIMIT 10000

        """

df = bq_assistant.query_to_pandas(QUERY)

print(df.head(3))
# trace1 = go.Scatter(
#
#                     )
#
# trace2 = go.Pie(
#
#                     )
#
# trace3 = go.Bar(
#
# )
# data = [trace1]
#
# layout = dict(
#               title = '',
#               xaxis= dict(title= ''),
#               yaxis=dict(title=''),
#              )
# fig = dict(data = [trace1], layout = layout)
# plot(fig)
