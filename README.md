
# 🧬 PubMed Paper Fetcher

A powerful and developer-friendly Python CLI tool to search for biomedical research papers on **PubMed** and filter them to find authors affiliated with **pharma or biotech companies** — perfect for research scouting, competitive analysis, or collaborations.



## 🚀 Features

✅ Flexible query support using PubMed's syntax  
✅ Extract author affiliations & corresponding emails  
✅ Filter **non-academic authors** using smart keyword heuristics  
✅ Export data as a clean CSV file  
✅ Built-in debug mode for transparency  
✅ Designed for automation and CLI integration



## 🧪 Example Usage

```bash
poetry run get-papers-list "covid-19 vaccine" -f results.csv -d
````

🔹 `"covid-19 vaccine"` is your PubMed search query
🔹 `-f results.csv` saves the output to a file
🔹 `-d` enables debug mode to view internal steps



## 📦 Installation

> Ensure [Poetry](https://python-poetry.org/docs/#installation) is installed on your system.

```bash
git clone https://github.com/YOUR_USERNAME/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install
```



## 🧠 How It Works

1. 🔎 Searches PubMed using your query (`esearch`)
2. 📄 Fetches detailed article metadata (`efetch`)
3. 🧪 Analyzes affiliations to identify **non-academic authors** using keyword filtering (`university`, `institute`, `college`, etc.)
4. 🏢 Extracts authors working in **pharma/biotech companies**
5. 📤 Outputs a structured table (and optionally, saves it to CSV)



## 📁 Project Structure

```
pubmed-paper-fetcher/
├── cli.py                    # CLI logic using argparse
├── pyproject.toml            # Poetry configuration
├── README.md                 # You’re here!
├── pubmed_paper_fetcher/
│   └── fetcher.py            # Core logic: API + parsing + filtering
└── results.csv               # Output file (generated)
```



## 📊 Output Format

| Column                         | Description                       |
| ------------------------------ | --------------------------------- |
| **PubmedID**                   | Unique paper ID from PubMed       |
| **Title**                      | Research paper title              |
| **Publication Date**           | Year of publication               |
| **Non-academic Author(s)**     | Authors from pharma/biotech firms |
| **Company Affiliation(s)**     | Names of identified companies     |
| **Corresponding Author Email** | Author’s email, if available      |



## 🧰 Built With

* `requests` – PubMed API interaction
* `lxml` – XML parsing
* `pandas` – CSV generation
* `argparse` – Command-line handling
* `mypy` – Static typing
* `Poetry` – Dependency & script management



## 📌 Why This Project?

This tool is designed to help:

* 🧪 Research teams scouting for collaborators in industry
* 💊 Pharma firms analyzing competitive research trends
* 📊 Analysts filtering authors by affiliation
* 🎓 Students learning about real-world PubMed API usage



## 👩‍💻 Author

**Jahnavi Grandhi**
📧 [jahnavigrandhi2005@gmail.com](mailto:jahnavigrandhi2005@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/jahnavi-grandhi-a74a042a1/)






### ✅ To Use It:

1. Copy the entire block above.
2. Open your `README.md` file in VS Code.
3. Paste and save.
4. Run:



---

