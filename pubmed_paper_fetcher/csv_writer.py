from tabulate import tabulate
from typing import List, Dict

def clean_cell(value):
    """Convert list/dict/None to clean single-line string for display."""
    if isinstance(value, list):
        return "; ".join(str(clean_cell(v)) for v in value)
    if isinstance(value, dict):
        return ", ".join(f"{k}: {v}" for k, v in value.items())
    if value is None:
        return "N/A"
    return str(value).replace("\n", " ").replace("\r", "").strip()

def write_ascii_table_to_file(data: List[Dict], filename: str):
    if not data:
        print("⚠️ No data to write.")
        return

    headers = list(data[0].keys())
    rows = [[clean_cell(row.get(h)) for h in headers] for row in data]

    # Only write the ASCII table to file
    ascii_table = tabulate(rows, headers=headers, tablefmt="grid")

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(ascii_table)

    # Also show in terminal
    print("\n📄 PubMed Results:\n")
    print(ascii_table)
    print(f"\n✅ Results saved to '{filename}'")
