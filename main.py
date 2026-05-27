from etl.extract import extract
from etl.transform import transform
from etl.load import load

df = extract("data/sales.csv")
df = transform(df)
load(df)