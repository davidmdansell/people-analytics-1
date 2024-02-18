import pandas as pd

# Load the Excel file
file_path = '/Users/davidansell/Documents/GitHub/people-analytics-1/people-analytics-test/hiring demand tool;.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()
# Display the dataframe
print(data)


# Dropping 'talent community', 'level', and 'full year' columns as they are not needed for the requested visualization
data_reduced = data.drop(columns=['talent community', 'level', 'full year'])

# Aggregating monthly data
monthly_columns = ['sept', 'oct', 'nov', 'dec', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug']
monthly_data = data_reduced.groupby(['region', 'country'])[monthly_columns].sum().reset_index()

# Aggregating quarterly data
quarterly_columns = ['q1', 'q2', 'q3', 'q4']
quarterly_data = data_reduced.groupby(['region', 'country'])[quarterly_columns].sum().reset_index()

monthly_data.head(), quarterly_data.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetics for the plots
sns.set_style("whitegrid")

# Function to plot monthly hiring demand trends for each country within a region
def plot_monthly_demand_by_region(region, data):
    # Filter data for the specified region
    region_data = data[data['region'] == region]
    
    # Setting up the plot
    plt.figure(figsize=(14, 6))
    plt.title(f'Monthly Hiring Demand in {region}')
    
    # Plotting each country's monthly demand
    for index, row in region_data.iterrows():
        plt.plot(monthly_columns, row[monthly_columns], marker='o', label=row['country'])
    
    plt.xticks(rotation=45)
    plt.ylabel('Hiring Demand')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Get a list of unique regions to plot for each
unique_regions = monthly_data['region'].unique()

# Plotting for the first region as an example
plot_monthly_demand_by_region(unique_regions[0], monthly_data)
