import pandas as pd

# Explicitly define all columns as strings
df = pd.read_csv(
    "GJ_anyror_village_data.txt",
    dtype=str
)

# Export to JSON with Unicode and indentation
df.to_json(
    "GJ_anyror_village_data.json",
    orient="records",
    force_ascii=False,
    indent=2
)
