# Trend Monitoring Dashboard

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('trends.csv')

# Basic Exploration
print(df.head())

# Aggregation
category_summary = df.groupby("category")["mentions"].sum()
print(category_summary)

# Visualization
category_summary.plot(kind="bar", title="Mentions by Category")
plt.show()
