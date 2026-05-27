def transform(df):
    df["amount_eur"] = df["amount"] * 0.93
    return df