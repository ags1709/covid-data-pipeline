import sqlite3

def save_to_sqlite(df, db_name="data/covid.db"):
    conn = sqlite3.connect(db_name)
    
    df.to_sql("denmark_covid", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data saved to {db_name}")