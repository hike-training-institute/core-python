import psycopg2 as pg
import pandas as pd
import matplotlib
connection = pg.connect(user = "postgres",
                          password = "postgres",
                          host = "127.0.0.1",
                          port = "5432",
                          database = "stock")

df = pd.read_sql('select * from fundamental', connection)
print(df.head())
df.head().plot('bv_sh', 'mkt_cap', kind='scatter')