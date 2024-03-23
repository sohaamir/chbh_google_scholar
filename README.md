# Extracting and predicting Google Scholar citations using beautifulsoup4, SerpAPI and Prophet

This directory contains code for the extraction and forecasting of Google Scholar data for researchers at the Centre for Human Brain Health (CHBH), University of Birmingham.

Specficially, this involves

- Scraping a list of researchers at the CHBH from the CHBH website (using `beautifulsoup4` ).
- Extracting Google Scholar statistics including citation data (using `serpapi` ).
- Forecasting citations for the years 2024, 2025 and 2026 (using `prophet`).

## Directory structure

```
├── README.md
├── code
│   ├── extract_scholar_info.py
│   ├── json_to_csv.py
│   ├── processing_citation_data.py
│   └── scrape_chbh.py
├── data
│   ├── chbh_google_scholar_statistics
│   │   ├── (42 individual json files, 1 for each person)
│   ├── citation_statistics
│   │   ├── citation_statistics.csv
│   │   └── citation_statistics_with_predictions.csv
│   └── names_and_ids
│       ├── chbh_names.json
│       ├── filtered_names_and_citation_ids.csv
│       ├── names.json
│       └── names_and_citation_ids.csv
├── notebooks
│   ├── citations_plot.png
│   └── plotting_chbh_statistics.ipynb
├── plots
│   ├── Lei Zhang_citations_per_year.html
│   ├── Lei Zhang_cumulative_citations.html
│   └── citations_plot.png
└── requirements.txt
```

## Setting up the environment

Here are instructions on how to set up your environment:

Firstly, download the repository to your local machine, creating a `virtualenv` within.

```python
git clone https://github.com/sohaamir/chbh_google_scholar.git
python3 -m venv .venv
source .venv/bin/activate
which python
/path/chbh_google_scholar/.venv/bin/python
```

Then install the requirements which are:

```pip install -r requirements.txt```

```python
requests
beautifulsoup4
pandas
serpapi
matplotlib
prophet
ipykernel
traitlets
plotly
jupyter
```

### Extracting data from the CHBH website

We can use `beautifulsoup4` to extract names from six pages on the CHBH website that list senior researchers. Initally, this kept their title (e.g., Dr, Professor) so I added some additional code to remove this.

```python
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
```

This gives us a list of CHBH researchers we can use as input into `serpapi`.

```json
{
  "chbh-investigators": [
    "Alan Wing",
    "Andrea Krott",
    "Kim Shapiro",
    "Craig McAllister",
    "Clare Anderson",
    "Rachel Upthegrove",
    "Dietmar Heinke",
    "Lei Zhang",
    "Magda Chechlacz",
    "Joseph Galea",
    "Massimiliano (Max) Di Luca",
    "Jennifer Cook",
    "Matthew Apps",
    "KyungMin An",
    "Katja Kornysheva",
    "Andrew J. Bremner",
    "Ali Mazaheri",
    "Hamid Dehghani",
    "Damian Cruse",
    "Patricia Lockwood",
    "Ned Jenkinson",
    "Tom Rhys Marshall",
    "Chris Miall",
    "Stephane De Brito",
    "Romy Froemer",
    "Anna Kowalczyk",
    "Suzanne Higgs",
    "Sarah Aldred",
    "Andrew Bagshaw",
    "Rickson C. Mesquita",
    "Martin Wilson",
    "Davinia Fernández-Espejo",
    "Andrew Quinn",
    "Hyojin Park",
    "Karen Mullinger",
    "Arkady Konovalov",
    "Felipe Orihuela-Espina",
    "Carmel Mevorach",
    "Paul Muhle-Karbe",
    "Clayton Hickey",
    "Katrien Segaert",
    "Nick Holmes",
    "Sam Lucas",
    "Ole Jensen",
    "Barbara Pomiechowska",
    "Jian Liu",
    "Steven Frisson"
  ]
}
```



## Extracting Google Scholar data using SerpAPI

SerpAPI offers a range of APIs for Google services, including Scholar. It has a free tier, but restricts users to only 100 calls per month, so use them wisely!

### Working with the Jupyter Notebook for plotting

Install a kernel for Jupyter Notebooks within the virtual environment:

```python
 python -m ipykernel install --user --name=.venv
```

and then run the Jupyter Notebook:

```python
python -m notebook
```



