from etl.extract import extract
from etl.transform import transform, add_kpi
from etl.load import load

df = extract("data/sales.csv")
df = transform(df)
df = add_kpi(df)
load(df)