def load(df):
    result = df.groupby("region")["amount_eur"].sum()
    print(result)
    return result
    