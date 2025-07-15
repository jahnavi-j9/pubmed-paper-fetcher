# cli.py

import argparse
import pandas as pd
from pubmed_paper_fetcher.fetcher import fetch_results

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers by query.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-f", "--file", type=str, help="Output filename (.csv)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        print(f"Running query: {args.query}")

    results = fetch_results(args.query)

    if args.debug:
        print(f"Found {len(results)} results")

    df = pd.DataFrame(results)

    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()
