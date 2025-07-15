from typing import List, Dict
import requests
import xml.etree.ElementTree as ET
from pubmed_paper_fetcher.csv_writer import write_ascii_table_to_file

# API endpoints
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Identify non-academic affiliations
def is_non_academic(aff: str) -> bool:
    keywords = ["university", "college", "institute", "school", "hospital", "center", "centre", "lab"]
    return not any(k in aff.lower() for k in keywords)

# Step 1: Fetch PubMed IDs
def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    response = requests.get(PUBMED_SEARCH_URL, params={
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    })
    response.raise_for_status()

    data = response.json()
    print("DEBUG: Raw API response:", data)  # 🟢 Add this line
    return data.get("esearchresult", {}).get("idlist", [])


# Step 2: Fetch details for each paper
def fetch_paper_details(pubmed_ids: List[str]) -> str:
    if not pubmed_ids:
        return ""
    response = requests.get(PUBMED_FETCH_URL, params={
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    })
    response.raise_for_status()
    return response.text

# Step 3: Parse XML and structure output
def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    if not xml_data.strip():
        print("⚠️ No XML data received. Skipping parsing.")
        return []

    root = ET.fromstring(xml_data)
    articles = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.findtext(".//PMID") or "N/A"
        title = article.findtext(".//ArticleTitle") or "N/A"

        pub_date_tag = article.find(".//PubDate")
        pub_date = "N/A"
        if pub_date_tag is not None:
            y = pub_date_tag.findtext("Year")
            m = pub_date_tag.findtext("Month")
            d = pub_date_tag.findtext("Day")
            pub_date = "-".join(filter(None, [y, m, d]))

        authors: List[str] = []
        company_affiliations: List[str] = []
        corresponding_email = "N/A"

        for author in article.findall(".//Author"):
            first = author.findtext("ForeName", "")
            last = author.findtext("LastName", "")
            full_name = f"{first} {last}".strip()

            affs = [
                aff.text.strip() for aff in author.findall(".//AffiliationInfo/Affiliation")
                if aff is not None and aff.text
            ]

            non_academic = [aff for aff in affs if is_non_academic(aff)]
            if non_academic:
                authors.append(full_name)
                company_affiliations.extend(non_academic)

                if corresponding_email == "N/A":
                    for aff in non_academic:
                        if "@" in aff:
                            corresponding_email = aff.split()[-1]
                            break

        articles.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(authors) or "N/A",
            "Company Affiliation(s)": "; ".join(set(company_affiliations)) or "N/A",
            "Corresponding Author Email": corresponding_email
        })

    return articles

# Step 4: Prompt user query and write result to file
if __name__ == "__main__":
    query = input("🔍 Enter your PubMed search query: ").strip()
    pubmed_ids = fetch_pubmed_ids(query)

    if not pubmed_ids:
        print("❌ No results found for the query.")
    else:
        xml_data = fetch_paper_details(pubmed_ids)
        paper_results = parse_pubmed_xml(xml_data)

        output_path = "results.csv"
        write_ascii_table_to_file(paper_results, output_path)
