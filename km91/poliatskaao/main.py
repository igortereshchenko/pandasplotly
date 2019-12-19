import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"


from bq_helper import BigQueryHelper
# import plotly.graph_objs as go
# from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','san_francisco')

QUERY = """
        SELECT unique_key, resolution, pddistrict, pdid FROM bigquery-public-data.san_francisco.sfpd_incidents
        LIMIT 10000
        """
df = bq_assistant.query_to_pandas(QUERY)
print(df.head(3))


