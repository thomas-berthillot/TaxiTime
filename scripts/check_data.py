import pandas as pd

df = pd.read_csv(
    "data/processed/jfk_taxiout_2025.csv"
)

print("\n--- Dataset information ---")

print(df.info())

print("\n--- TaxiOut statistics ---")

print(df["TaxiOut"].describe())

print("\n--- Missing values ---")

print(
    df.isna()
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Airlines ---")

print(df["Reporting_Airline"].value_counts())

print("\n--- Aircraft registrations ---")

print("Unique registrations:", df["Tail_Number"].nunique())

print("\n--- Flight dates ---")

print(df["FlightDate"].min())
print(df["FlightDate"].max())