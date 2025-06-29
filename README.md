# COVID-19 Data Pipeline

A simple ETL project that extracts COVID-19 data from [Our World in Data](https://ourworldindata.org/), transforms it, and loads it into a sqlite3 .db file for future analysis.

## Features of the project
- Extracts data using HTTP requests
- Selects key features and filters for a specific country (Denmark)
- Saves the processed data to a sqlite3 .db file


## Running the project
To run the code first navigate to the project folder. Make sure all requirements are installed. Check the requirements.txt file, or simply run the command
```bash
pip install -r requirements.txt
```

After the requirements are installed, simply run the following command in the terminal
```bash
python main.py