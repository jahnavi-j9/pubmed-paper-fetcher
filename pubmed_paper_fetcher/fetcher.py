from typing import List, Dict, Optional
import requests
import xml.etree.ElementTree as ET

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital", "center", "centre", "lab"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def fetch_pubmed_ids(query: str) -> List[str]:
    url = f"{BASE_URL}/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 20}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(pubmed_id: str) -> Optional[Dict[str, str]]:
    url = f"{BASE_URL}/efetch.fcgi"
    params = {"db": "pubmed", "id": pubmed_id, "retmode": "xml"}
    response = requests.get(url, params=params)
    root = ET.fromstring(response.content)

    article = root.find(".//PubmedArticle")
    if not article:
        return None

    title = article.findtext(".//ArticleTitle", default="N/A")
    pub_date = article.findtext(".//PubDate/Year", default="N/A")

    authors_elem = article.findall(".//Author")
    non_academic_authors = []
    affiliations = set()
    email = "N/A"

    for author in authors_elem:
        affiliation_elem = author.find("AffiliationInfo/Affiliation")
        if affiliation_elem is not None:
            affiliation = affiliation_elem.text or ""
            if is_non_academic(affiliation):
                name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()
                non_academic_authors.append(name)
                affiliations.add(affiliation)
                if "@" in affiliation and email == "N/A":
                    email = affiliation.split()[-1]

    return {
        "PubmedID": pubmed_id,
        "Title": title,
        "Publication Date": pub_date,
        "Non-academic Author(s)": "; ".join(non_academic_authors),
        "Company Affiliation(s)": "; ".join(affiliations),
        "Corresponding Author Email": email
    }

def fetch_results(query: str) -> List[Dict[str, str]]:
    ids = fetch_pubmed_ids(query)
    return [paper for pid in ids if (paper := fetch_paper_details(pid))]
