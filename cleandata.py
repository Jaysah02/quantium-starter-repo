import pandas as pd
import os

folder_path = "data"
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

all_data = []

for file in csv_files:
    df = pd.read_csv(os.path.join(folder_path, file))

    # Filter only 'pink morsel'
    df = df[df['product'].str.lower() == 'pink morsel']

    # Remove '$' and convert price to float
    df['price'] = df['price'].str.replace('$', '').astype(float)

    # Calculate sales
    df['sales'] = df['quantity'] * df['price']

    # Keep only required columns
    df = df[['sales', 'date', 'region']]

    all_data.append(df)

# Combine and save
final_df = pd.concat(all_data)
final_df.to_csv("output.csv", index=False)
print("✅ Data cleaned and saved to output.csv")
