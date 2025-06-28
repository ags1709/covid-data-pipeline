# COVID-19 Data Pipeline

A simple ETL project that extracts COVID-19 data from [Our World in Data](https://ourworldindata.org/), transforms it, and loads it into a sqlite3 .db file for future analysis.

## Features of the project
- Extracts data using HTTP requests
- Selects key metrics and filters it for a specific country (Denmark)
- Saves the processed data to a sqlite3 .db file


## Running the project
To run the code simply navigate to the project folder and run the following command in the terminal

```bash
python main.py