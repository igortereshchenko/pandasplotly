# import os
# import pandas as pd
# from bq_helper import BigQueryHelper
# import plotly.graph_objs as go
# from plotly.offline import plot
# os.environ["GOOGLE_APPLICATION_CREDENRIALS"]="keys.json"
# from google.cloud import bigquery
# client =bigquery.Client()
# data_ref=client.dataset('san_francisco',project='bigquery-public-data')
# bg_asisten=BigQueryHelper('bigquery-public-data','san_francisco')
# QUERY = """
#         SELECT  FROM
#         LIMIT 10000
#         """
# df=bg_asisten.query_
# print(type(data_ref))

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','san_francisco')


QUERY = """
        SELECT unique_key, status,agency_name,created_date FROM `bigquery-public-data.san_francisco.street_trees`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)




female_df = df[df['status']=='closed'];

female_df_groupby = female_df.groupby(['agency_name'])[].sum()


trace1 = go.Scatter(
                    x = female_df_groupby.index,
                    y = female_df_groupby.values,
                    mode = "closed",
                    name = "agency",
                    )
print(df.head(10))
