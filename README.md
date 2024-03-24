# Extracting and predicting Google Scholar citations using beautifulsoup4, SerpAPI and Prophet

[![Analysis Guide](https://img.shields.io/badge/analysis-guide-blue?logo=markdown)](https://github.com/sohaamir/chbh_google_scholar/blob/main/analysis_guide.md)
[![Static Badge](https://img.shields.io/badge/view-dataset-blue?style=flat&logo=kaggle&logoColor=turquoise)](https://www.kaggle.com/datasets/sohamir/citation-statistics-for-researchers-at-the-chbh)


This directory contains code for the extraction and forecasting of Google Scholar data for researchers at the Centre for Human Brain Health (CHBH), University of Birmingham.

Specficially, this involves:

- Scraping a list of researchers at the CHBH from the CHBH website (using `beautifulsoup4` ).
- Extracting Google Scholar statistics including citation data (using `serpapi` ).
- Forecasting citations for the years 2024, 2025 and 2026 (using `prophet`).

A more detailed guide on how to perform the analysis and a link to the dataset on Kaggle are available by clicking on the badges above.

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

Then install the requirements:

```pip install -r requirements.txt```

which are:

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

Ultimately, we are able to use `prophet` to forecast citation counts for the next three years (2024, 2025 and 2026), and plot these predictions with historical data:

<div align="center">
  <img src="https://github.com/sohaamir/chbh_google_scholar/blob/main/plots/lei_cumulative_plot.png" width="100%">
</div>
<br>

<div align="center">
  <img src="https://github.com/sohaamir/chbh_google_scholar/blob/main/plots/lei_yearly_plot.png" width="100%">
</div>
<br>
































