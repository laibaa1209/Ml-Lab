import pandas as pd

# 1. Define column names
columns = [
    "id", "diagnosis",
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
    "smoothness_mean", "compactness_mean", "concavity_mean",
    "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",

    "radius_se", "texture_se", "perimeter_se", "area_se",
    "smoothness_se", "compactness_se", "concavity_se",
    "concave_points_se", "symmetry_se", "fractal_dimension_se",

    "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
    "smoothness_worst", "compactness_worst", "concavity_worst",
    "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
]

# 2. Load the .data file
df = pd.read_csv(
    r"C:\Laiba\Uni\5th Sem\Ml-Lab\Lab 6\breast+cancer+wisconsin+diagnostic\wdbc.data",
    header=None,
    names=columns
)

# 3. Save as .csv
df.to_csv(
    r"C:\Laiba\Uni\5th Sem\Ml-Lab\Lab 6\breast+cancer+wisconsin+diagnostic\wdbc_clean.csv",
    index=False
)

print("CSV file created: wdbc_clean.csv")
