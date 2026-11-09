"""Import the raw SurveyPoint export into a clean CSV for analysis."""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "vendor-exports", "pulse-survey-FY2026-raw.csv")
OUTPUT = os.path.join(HERE, "survey-export.csv")

# SurveyPoint writes two preamble lines, separates with semicolons, and names its columns q1 to q5.
COLUMNS = {
    "resp_id": "Response_ID",
    "qtr": "Quarter",
    "rgn": "Region",
    "q1": "Rating",
    "q2": "Likes_Most",
    "q3": "Biggest_Issue",
    "q4": "Would_Pay_More_For",
    "q5": "Comment",
}

with open(RAW, encoding="utf-8") as handle:
    lines = [line for line in handle.read().splitlines() if line.strip()]

fieldnames = [COLUMNS[name] for name in lines[2].split(";")]
rows = [dict(zip(fieldnames, line.split(";"))) for line in lines[3:]]

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Imported {len(rows)} responses into {os.path.basename(OUTPUT)}")
