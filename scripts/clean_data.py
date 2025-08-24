import pandas as pd
import numpy as np
from pathlib import Path

# Paths
input_path = Path("C:/ALL-CASE-STUDIES-DONE/flight-delay-case-study/data/Flight_delay.csv")
output_path = Path("C:/ALL-CASE-STUDIES-DONE/flight-delay-case-study/data/cleaned_flight_delay.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Load Data
df = pd.read_csv(input_path, dtype=str)
print(f"🔄 Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns")
print("📋 Available columns:", df.columns.tolist())

# Step 1: Rename columns to snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("/", "_")

# Step 2: Convert 'date' column to datetime
if 'date' in df.columns:
    df['fl_date'] = pd.to_datetime(df['date'], errors='coerce')
else:
    print("⚠️ 'date' column not found. Skipping date conversion and related steps.")

# Step 3: Replace blanks and common placeholders with NaN
df.replace(["", " ", "Not Available", "NA", "NaN", "N/A"], pd.NA, inplace=True)

# Step 4: Convert numeric columns (based on actual column names)
numeric_cols = [
    'depdelay', 'arrdelay', 'weatherdelay', 'securitydelay',
    'carrierdelay', 'nasdelay', 'lateaircraftdelay', 'cancelled', 'diverted'
]
available_numeric_cols = [col for col in numeric_cols if col in df.columns]

if available_numeric_cols:
    for col in available_numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df[available_numeric_cols] = df[available_numeric_cols].fillna(0)
else:
    print("⚠️ No matching numeric columns found. Skipping numeric cleaning.")

# Step 5: Fill missing categorical values if the columns exist
for cat_col, default in [('cancellationcode', 'Not Cancelled'), 
                         ('airline', 'Unknown'), 
                         ('origin', 'Unknown'), 
                         ('dest', 'Unknown')]:
    if cat_col in df.columns:
        df[cat_col] = df[cat_col].fillna(default)

# Step 6: Feature engineering
if set(['weatherdelay', 'securitydelay', 'carrierdelay', 'nasdelay', 'lateaircraftdelay']).issubset(df.columns):
    df['total_delay'] = df[['weatherdelay', 'securitydelay', 'carrierdelay', 'nasdelay', 'lateaircraftdelay']].sum(axis=1)
else:
    df['total_delay'] = 0  # Fallback

if 'arrdelay' in df.columns:
    df['is_delayed'] = df['arrdelay'] > 15
else:
    df['is_delayed'] = False

if set(['origin', 'dest']).issubset(df.columns):
    df['flight_route'] = df['origin'] + "-" + df['dest']
else:
    df['flight_route'] = "Unknown"

if 'fl_date' in df.columns:
    df['weekday_name'] = df['fl_date'].dt.day_name()
else:
    df['weekday_name'] = "Unknown"

# Step 7: Flag duplicates
df['is_duplicate'] = df.duplicated()
num_duplicates = df['is_duplicate'].sum()
print(f"⚠️ Found {num_duplicates} duplicate rows (flagged, not dropped)")

# Step 8: Summary
if 'total_delay' in df.columns:
    print("\n📊 Summary of cleaned numeric data:")
    print(df[available_numeric_cols + ['total_delay']].describe())

# Step 9: Save cleaned dataset
df.to_csv(output_path, index=False)
print(f"\n✅ Cleaned data saved to: {output_path.resolve()}")
