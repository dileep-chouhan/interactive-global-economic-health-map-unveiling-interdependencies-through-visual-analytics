import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# --- 1. Synthetic Data Generation ---
np.random.seed(42)  # for reproducibility
num_countries = 10
num_years = 5
countries = [f'Country {i+1}' for i in range(num_countries)]
years = range(2019, 2019 + num_years)
data = {
    'Country': [],
    'Year': [],
    'GDP': [],
    'Inflation': [],
    'Unemployment': []
}
for country in countries:
    for year in years:
        data['Country'].append(country)
        data['Year'].append(year)
        data['GDP'].append(np.random.randint(1000, 10000))
        data['Inflation'].append(np.random.uniform(1, 5))
        data['Unemployment'].append(np.random.uniform(2, 10))
df = pd.DataFrame(data)
# --- 2. Analysis ---
# (Simplified analysis for demonstration;  a real-world project would involve more sophisticated analysis)
# Calculate average GDP growth per country
average_gdp_growth = df.groupby('Country')['GDP'].mean()
# Calculate correlation between GDP and Inflation
correlation_gdp_inflation = df['GDP'].corr(df['Inflation'])
# --- 3. Visualization ---
# Matplotlib Scatter Plot (GDP vs Inflation)
plt.figure(figsize=(8, 6))
plt.scatter(df['GDP'], df['Inflation'])
plt.title('GDP vs. Inflation')
plt.xlabel('GDP')
plt.ylabel('Inflation')
plt.savefig('gdp_inflation_scatter.png')
print("Plot saved to gdp_inflation_scatter.png")
# Seaborn Bar Plot (Average GDP Growth)
plt.figure(figsize=(10, 6))
sns.barplot(x=average_gdp_growth.index, y=average_gdp_growth.values)
plt.title('Average GDP Growth per Country')
plt.xlabel('Country')
plt.ylabel('Average GDP')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('average_gdp_growth.png')
print("Plot saved to average_gdp_growth.png")
# Plotly Interactive Map (Example - requires geographic data for a real map)
#  This is a placeholder;  replace with actual geographic data for a functional map.
fig = px.scatter_geo(df, locations="Country", locationmode='country names', 
                     color="GDP", size='GDP', hover_name="Country", 
                     range_color=[df['GDP'].min(), df['GDP'].max()],
                     title='Interactive GDP Map (Placeholder)') #Requires lat/lon data for proper functionality
fig.update(layout_coloraxis_showscale=False)
fig.write_image("interactive_gdp_map.png")
print("Plot saved to interactive_gdp_map.png")
print(f"Correlation between GDP and Inflation: {correlation_gdp_inflation:.2f}")