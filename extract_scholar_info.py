import serpapi
import json
import pandas as pd

# This script extracts information from Google Scholar using the SerpApi API. It iterates through the list of citation IDs and 
# saves the results in a JSON file for each citation ID. The data can then be processed and analyzed further.
def author_results(author_id):
    print(f"Extracting author results for author ID: {author_id}")

    params = {
        "api_key": "SERP_API_KEY",  # Replace with your actual SerpApi API key
        "engine": "google_scholar_author",  # Author results search engine
        "author_id": author_id,  # Author ID as function input
        "hl": "en"
    }
    
    search = serpapi.search(params) 
    results = search  # Directly use the 'results'

    # Extract the necessary information
    thumbnail = results.get("author", {}).get("thumbnail")
    name = results.get("author", {}).get("name")
    affiliations = results.get("author", {}).get("affiliations")
    email = results.get("author", {}).get("email")
    website = results.get("author", {}).get("website")
    interests = results.get("author", {}).get("interests")
    
    cited_by_table = results.get("cited_by", {}).get("table")
    cited_by_graph = results.get("cited_by", {}).get("graph")
    
    public_access_link = results.get("public_access", {}).get("link")
    available_public_access = results.get("public_access", {}).get("available")
    not_available_public_access = results.get("public_access", {}).get("not_available")
    co_authors = results.get("co_authors")
    
    author_results_data = {
      "thumbnail": thumbnail,
      "name": name,
      "affiliations": affiliations,
      "email": email,
      "website": website,
      "interests": interests,
      "cited_by_table": cited_by_table,
      "cited_by_graph": cited_by_graph,
      "public_access_link": public_access_link,
      "available_public_access": available_public_access,
      "not_available_public_access": not_available_public_access,
      "co_authors": co_authors
    }
    
    # Save the data to a JSON file named after the author_id
    with open(f"{author_id}.json", 'w', encoding='utf-8') as f:
        json.dump(author_results_data, f, ensure_ascii=False, indent=4)
    
    print(f"Data saved to {author_id}.json")
    return author_results_data 

# Load the CSV file (make sure the path is correct)
df = pd.read_csv("filtered_names_and_citation_ids.csv")

# Run through the entire CSV file
df_limited = df.head(42)

# Iterate through the citation IDs
for index, row in df_limited.iterrows():
    author_id = row['citation_id']
    data = author_results(author_id)
