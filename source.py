import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crop_fertilizer_file = '/content/Crop_and_fertilizer_with_usage.csv'
crop_data = pd.read_csv(crop_fertilizer_file)

print("Dataset Information:")
crop_data.info()
print("\nFirst 5 rows:")
print(crop_data.head())

print("\nMissing values:")
print(crop_data.isnull().sum())

print("\nDescriptive statistics:")
print(crop_data.describe())

plt.figure(figsize=(12, 6))
sns.barplot(data=crop_data, x='Crop', y='Fertilizer_Usage', hue='Fertilizer')
plt.xticks(rotation=90)
plt.xlabel('Crop')
plt.ylabel('Fertilizer Usage (kg/ha)')
plt.title('Fertilizer Usage by Crop')
plt.legend(title='Fertilizer Type')
plt.show()

water_risk_notebook = '/content/Crop_and_fertilizer_with_usage.csv'

