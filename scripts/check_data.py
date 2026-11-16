import pandas as pd

df = pd.read_csv("data/processed/jfk_taxiout_2025.csv")

print("\n--- Dataset information ---")
df.info()

print("\n--- TaxiOut statistics ---")
print(df["TaxiOut"].describe())

print("\n--- Missing values ---")
print(df.isna().sum().sort_values(ascending=False))

print("\n--- Airlines ---")
print(df["Reporting_Airline"].value_counts())

print("\n--- Aircraft registrations ---")
print("Unique registrations:", df["Tail_Number"].nunique())

print("\n--- Flight dates ---")
print(df["FlightDate"].min())
print(df["FlightDate"].max())

count = 0
for x in df.duplicated():
    if x != False:
        count = count + 1;

print("\n--- Duplicates Rows ---")
print("Number of duplicates: ", count)

print("\n--- Quantiles ---")
print("1%: ", df["TaxiOut"].quantile(0.01))
print("5%: ", df["TaxiOut"].quantile(0.05))
print("10%: ", df["TaxiOut"].quantile(0.1))
print("90%: ", df["TaxiOut"].quantile(0.9))
print("95%: ", df["TaxiOut"].quantile(0.95))
print("99%: ", df["TaxiOut"].quantile(0.99))

print("\n--- Longest TaxiOut ---")
longest_30 = df.nlargest(30, 'TaxiOut')
for index, row in longest_30.iterrows():
    taxi = row['TaxiOut']
    month = row['Month']
    day = row['DayofMonth']
    print(f"Longest TaxiOut : {taxi} (Mois : {month}, Jour du mois : {day})")

print("\n--- Smallest TaxiOut ---")
smallest_30 = df.nsmallest(30, 'TaxiOut')
for index, row in smallest_30.iterrows():
    taxi = row['TaxiOut']
    month = row['Month']
    day = row['DayofMonth']
    print(f"Smallest TaxiOut : {taxi} (Mois : {month}, Jour du mois : {day})")