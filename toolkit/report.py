import csv
from dataclasses import asdict
from toolkit.reader import RowError



def write_error_report(error_list: list[RowError], path: str) -> None:
    with open(path, "w", newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ["line","reason"]
        )
        writer.writeheader()
        for row in sorted(error_list,key=lambda e: e.line):
            writer.writerow(asdict(row))
