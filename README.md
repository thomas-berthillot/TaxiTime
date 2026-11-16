# TaxiTime

**Personal project — Machine Learning & Data Analysis**

TaxiTime is a machine learning project focused on predicting aircraft taxi-out times at John F. Kennedy International Airport (JFK).

The goal is to estimate how long an aircraft will spend taxiing between leaving its gate and taking off, using historical flight data and information available before departure.

**Status: In progress**

## Objective

Taxi-out times can vary depending on traffic, departure schedules, airline operations and airport conditions.

TaxiTime explores whether historical flight data can be used to predict these durations.

## Dataset

The project uses the **Reporting Carrier On-Time Performance** dataset provided by the US Bureau of Transportation Statistics (BTS).

The dataset contains historical flight information, including:
- Scheduled departure times
- Airlines and flight numbers
- Origin and destination airports
- Aircraft information
- Actual departure times
- Taxi-out durations
- Flight cancellations and delays

### Current dataset

- Year: 2025
- Source: Bureau of Transportation Statistics
- Period: January to December 2025
- Format: Monthly ZIP archives containing CSV files
- Airport: JFK (`Origin == "JFK"`)

The dataset only covers flights included in the BTS reporting system.

### 1. Data preparation

- Load the monthly BTS archives.
- Combine the monthly datasets.
- Filter flights departing from JFK.
- Inspect missing values and inconsistent records.
- Prepare the dataset for analysis.

### 2. Exploratory Data Analysis

The next step is to understand how taxi-out times vary.

Areas to investigate include:
- Departure time and time of day
- Day of the week
- Seasonal patterns
- Airline differences
- Destination differences
- Distribution of taxi-out durations

## Technologies

### Currently used
- Python
- Pandas

### Planned
- NumPy
- Matplotlib
- Scikit-learn

## Project structure

```text
TaxiTime/
├── data/
│   ├── raw/
│   │   └── bts/
│   ├── processed/
│   └── sample/
├── models/
├── notebooks/
├── scripts/
├── src/
├── README.md
└── requirements.txt
```

Raw datasets and the Python virtual environment are kept outside the Git repository.

## Data sources

- [BTS — Reporting Carrier On-Time Performance](https://www.transtats.bts.gov/TableInfo.asp?QO_fu146_anzr=b0-gvzr&gnoyr_VQ=FGJ)
- [BTS — Dataset field definitions](https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FGJ)
- [BTS — Monthly data archives](https://www.transtats.bts.gov/PREZIP/)

## Current progress

- [x] Download the 12 monthly BTS archives for 2025
- [x] Set up the Python environment and project structure
- [ ] Complete and validate data preprocessing
- [ ] Exploratory data analysis
- [ ] Feature engineering
- [ ] Train baseline and regression models
- [ ] Evaluate and compare model performance
- [ ] Document final results