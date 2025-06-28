from etl.extract import fetch_covid_data
from etl.transform import transform_covid_data
from etl.load import save_to_sqlite

def run_pipeline():
    df_raw = fetch_covid_data()
    df_transformed = transform_covid_data(df_raw)
    save_to_sqlite(df_transformed, "data/covid.db")


if __name__ == "__main__":
    run_pipeline()
