import pandas as pd
import os

# Step 1: List all CSV files
folder_path = "data"
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Step 2: Read and clean each file
all_data = []

for file in csv_files:
    df = pd.read_csv(os.path.join(folder_path, file))

    # Filter for Pink Morsel
    df = df[df['product'] == 'Pink Morsel']

    # Add sales column
    df['sales'] = df['quantity'] * df['price']

    # Keep only required columns
    df = df[['sales', 'date', 'region']]

    all_data.append(df)

# Step 3: Combine all cleaned data
final_df = pd.concat(all_data)

# Step 4: Save to output CSV
final_df.to_csv("output.csv", index=False)
print("✅ Data cleaned and saved to output.csv")
