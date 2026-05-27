def transform(df):
    df["amount_eur"] = df["amount"] * 0.90
    return df

def add_kpi(df):
    df["high_value"] = df["amount"] > 250
    return df