import os
import json
import pandas as pd

# List all JSON files in the current directory
json_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.json')]

# Initialize a list to store data for each author
authors_data = []

# Process each JSON file
for filename in json_files:
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        # Extracting required information
        name = data['name']
        citations_all = next((item for item in data['cited_by_table'] if 'citations' in item), {}).get('citations', {}).get('all', 0)
        h_index_all = next((item for item in data['cited_by_table'] if 'h_index' in item), {}).get('h_index', {}).get('all', 0)
        i10_index_all = next((item for item in data['cited_by_table'] if 'i10_index' in item), {}).get('i10_index', {}).get('all', 0)
        
        # Initialize a dict for the author's citation years data
        citation_years = {'name': name, 'citations': citations_all, 'h-index': h_index_all, 'i10-index': i10_index_all}
        
        # Add citation count per year to the dict
        for item in data['cited_by_graph']:
            year = item['year']
            citations = item['citations']
            citation_years[f'citations_{year}'] = citations
        
        # Append the author's data to the list
        authors_data.append(citation_years)

# Convert the list of data into a DataFrame
df = pd.DataFrame(authors_data)

# Fill NaN values with 0 to indicate years without citations
df.fillna(0, inplace=True)

# Save the DataFrame to a CSV file
df.to_csv('../data/citations_statistics/citation_statistics.csv', index=False, encoding='utf-8')
