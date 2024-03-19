import requests
from bs4 import BeautifulSoup
import json

def scrape_names_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements that contain names - this will need to be customized based on the page's HTML structure
    name_elements = soup.find_all('h2')  # Assuming names are within <h2> tags, change as needed

    names = [elem.get_text(strip=True) for elem in name_elements]
    return names

# List of URLs to scrape
urls = [
    "https://www.birmingham.ac.uk/research/centre-for-human-brain-health/chbh-research-themes/lifespan-and-brain-health",
    "https://www.birmingham.ac.uk/research/centre-for-human-brain-health/chbh-research-themes/cognitive-computational-neuroscience",
    "https://www.birmingham.ac.uk/research/centre-for-human-brain-health/chbh-research-themes/social-interaction-and-communication",
    "https://www.birmingham.ac.uk/research/centre-for-human-brain-health/chbh-research-themes/learning-memory-and-performance",
    "https://www.birmingham.ac.uk/research/centre-for-human-brain-health/chbh-research-themes/awareness-consciousness-and-sleep",
    "https://www.birmingham.ac.uk/research/centre-for-human-brain-health/chbh-research-themes/neuroimaging-methods-and-ai"
]

# Initialize an empty set to hold all unique names across themes
unique_names = set()

# Scrape names from each URL
for url in urls:
    names = scrape_names_from_page(url)
    for name in names:
        if 'Dr ' in name or 'Professor ' in name:
            # Clean name and add to the set of unique names
            clean_name = name.replace('Dr ', '').replace('Professor ', '').strip()
            unique_names.add(clean_name)

# Convert the set of unique names to a list for JSON serialization
combined_list = list(unique_names)

# Create new dictionary with a single key for all investigators
combined_data = {"chbh-investigators": combined_list}

# Save the combined data to a new JSON file
with open('chbh_names.json', 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=2)