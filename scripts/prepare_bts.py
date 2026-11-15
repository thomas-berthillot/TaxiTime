from pathlib import Path
from zipfile import ZipFile

import pandas as pd

# Configuration variable
RAW_DIR = Path("data/raw/bts")
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "jfk_taxiout_2025.csv"
AIRPORT = "JFK"
CHUNK_SIZE = 100_000
COLUMNS = [
    "FlightDate",
    "Year",
    "Month",
    "DayofMonth",
    "DayOfWeek",
    "Reporting_Airline",
    "Tail_Number",
    "Flight_Number_Reporting_Airline",
    "Origin",
    "Dest",
    "CRSDepTime",
    "DepTime",
    "DepDelay",
    "TaxiOut",
    "WheelsOff",
    "Cancelled",
    "Diverted",
    "Distance",
]

if OUTPUT_FILE.exists():
    OUTPUT_FILE.unlink()

files = list(RAW_DIR.glob("On_Time_Reporting_Carrier_On_Time_Performance_1987_present_2025_*.zip"))
files = sorted(files, key=lambda path: int(path.stem.split('_')[-1]))

total_rows = 0
header = True

for x in files:
    with ZipFile(x, "r") as zip_ref:
        csv_files = [f for f in zip_ref.namelist() if f.endswith(".csv")]
        print(x)

        for y in csv_files:
            with zip_ref.open(y, mode='r', pwd=None) as file:
                chunks = pd.read_csv(file, usecols=COLUMNS, chunksize=CHUNK_SIZE, low_memory=False)

                for chunk in chunks:
                    chunk['TaxiOut'] = pd.to_numeric(chunk['TaxiOut'], errors='coerce')
                    chunk['Cancelled'] = pd.to_numeric(chunk['Cancelled'], errors='coerce')
                    chunk = chunk[(chunk['Origin'] == "JFK") & (chunk["Cancelled"] == 0) & (chunk["TaxiOut"].notna())]
                    chunk = chunk.dropna(axis=0, how='any')

                    chunk.to_csv(OUTPUT_FILE, sep=',', encoding='utf-8', index=False, header=header, mode='a', columns=COLUMNS)
                    header = False
                    total_rows = total_rows + chunk.shape[0]

    print(f"Total of rows in file : {total_rows}")