
# 🧬 PubMed Paper Fetcher

A Python CLI tool that fetches research papers from PubMed based on a search query, filters out papers with at least one **non-academic affiliation**, and outputs the results in a clean **CSV file** along with a **terminal ASCII table** preview.

> Useful for identifying papers with potential **industry involvement**, such as pharmaceutical or biotech affiliations.



## 📦 Features

- Query PubMed for recent papers using the E-utilities API
- Identify papers with **non-academic company affiliations**
- Extracts author names, affiliations, publication date, and contact email
- Saves results in `results.csv` in **tabular format**
- Pretty-prints results to terminal using `tabulate`



## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jahnavi-j9/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
````

### 2. Install dependencies using Poetry

Make sure Poetry is installed: [https://python-poetry.org/](https://python-poetry.org/)

```bash
poetry install
```



## 🧪 Usage

### ▶️ Run interactively

```bash
poetry run python pubmed_paper_fetcher/fetcher.py
```

You will be prompted to enter a search query (e.g., `covid vaccine`, `AI in medicine`, `cancer therapy`).

The results will be saved in `results.csv` and also displayed as a table in your terminal.



## 🛠 Output Example

```
🔍 Enter your PubMed search query: covid vaccine

📋 Results Preview:

+------------+---------------------------------------------------------------+--------------------+----------------------------+----------------------------------------+------------------------------+
| PubmedID   | Title                                                         | Publication Date   | Non-academic Author(s)     | Company Affiliation(s)                 | Corresponding Author Email   |
+------------+---------------------------------------------------------------+--------------------+----------------------------+----------------------------------------+------------------------------+
| 40640198   | Immunogenicity and protective efficacy...                     | 2025-Jul-10        | Corey P Mallett; J Zimmermann | Inspirevax Inc., Canada; GSK, USA   | N/A                          |
+------------+---------------------------------------------------------------+--------------------+----------------------------+----------------------------------------+------------------------------+
```



## 🧾 File Structure

```
pubmed-paper-fetcher/
│
├── pubmed_paper_fetcher/
│   ├── __init__.py
│   ├── fetcher.py            # Main script for running query and saving results
│   ├── csv_writer.py         # CSV writing and ASCII table logic
│
├── pyproject.toml            # Poetry configuration
├── README.md                 # You're reading this!
└── results.csv               # Output file after each run
```



## 🔍 Example Queries

* `covid vaccine`
* `AI in medicine`
* `cancer detection`
* `drug resistance`
* `biotech innovation`



## 💡 Filtering Logic

Affiliations **excluding** academic keywords such as:

```
["university", "college", "institute", "school", "hospital", "center", "centre", "lab"]
```

are considered **non-academic** (i.e., potentially company-related).



## 🙌 Author

[Jahnavi J9](https://github.com/jahnavi-j9)




