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

# Get a list of unique regions to plot for each
unique_regions = monthly_data['region'].unique()

# Plotting for the first region as an example
plot_monthly_demand_by_region(unique_regions[0], monthly_data)

# Filtering the original data for the first region
region_specific_data = data[data['region'] == unique_regions[0]]

# Aggregating hiring demand by level
demand_by_level = region_specific_data.groupby(['level'])[monthly_columns].sum().reset_index()

# Aggregating hiring demand by talent community
demand_by_community = region_specific_data.groupby(['talent community'])[monthly_columns].sum().reset_index()

demand_by_level.head(), demand_by_community.head()

# Function to plot hiring demand by level
def plot_demand_by_level(data):
    plt.figure(figsize=(14, 6))
    bottom = [0] * len(monthly_columns)  # Initialize bottom for stacked bar chart
    
    # Plotting each level
    for index, row in data.iterrows():
        plt.bar(monthly_columns, row[monthly_columns], bottom=bottom, label=row['level'])
        bottom = [bottom[i] + row[monthly_columns][i] for i in range(len(monthly_columns))]
    
    plt.title(f'Hiring Demand by Level in {unique_regions[0]}')
    plt.xticks(rotation=45)
    plt.ylabel('Hiring Demand')
    plt.legend(title='Level', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()


# Plotting hiring demand by level
plot_demand_by_level(demand_by_level)

# Function to plot hiring demand by talent community
def plot_demand_by_community(data):
    plt.figure(figsize=(14, 6))
    bottom = [0] * len(monthly_columns)  # Initialize bottom for stacked bar chart
    
    # Plotting each talent community
    for index, row in data.iterrows():
        plt.bar(monthly_columns, row[monthly_columns], bottom=bottom, label=row['talent community'])
        bottom = [bottom[i] + row[monthly_columns][i] for i in range(len(monthly_columns))]
    
    plt.title(f'Hiring Demand by Talent Community in {unique_regions[0]}')
    plt.xticks(rotation=45)
    plt.ylabel('Hiring Demand')
    plt.legend(title='Talent Community', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    

# Plotting hiring demand by talent community
plot_demand_by_community(demand_by_community)


# Filtering the data for ERP and Customer Relationship Management talent communities
erp_crm_data = data[data['talent community'].isin(['ERP', 'Customer Relationship Management'])]

# Aggregating hiring demand by country and talent community
erp_crm_demand_by_country = erp_crm_data.groupby(['country', 'talent community'])['full year'].sum().reset_index()

erp_crm_demand_by_country.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetics for the plots
sns.set_style("whitegrid")

# Creating a grouped bar chart
plt.figure(figsize=(14, 6))
sns.barplot(x='country', y='full year', hue='talent community', data=erp_crm_demand_by_country, palette='coolwarm')

plt.title('ERP vs Customer Relationship Management Hiring Demand by Country')
plt.xlabel('Country')
plt.ylabel('Full Year Hiring Demand')
plt.xticks(rotation=45)
plt.legend(title='Talent Community')
plt.tight_layout()

plt.show()
