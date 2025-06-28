import pandas as pd


def clean_covid_data(df, country="Denmark"):
    df_country = df[df["location"] == country].copy()

    df_country = df_country[["date", "location", "new_cases", "new_deaths", "total_cases"]].dropna()

    # df_country["date"] = pd.to_datetime(df_country["date"])
    df_country = df_country.sort_values("date")

    return df_country