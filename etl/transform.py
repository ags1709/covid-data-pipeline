import pandas as pd


def transform_covid_data(df, country="Denmark"):
    print("Transforming data ...")

    df_country = df[df["location"] == country].copy()

    df_country = df_country[["date", "location", "new_cases", "new_deaths", "total_cases"]].dropna()

    df_country = df_country.sort_values("date")

    print("Data transformed\n")
    return df_country