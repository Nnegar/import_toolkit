from toolkit.report import write_error_report
from toolkit.dedupe import find_duplicates
from toolkit.reader import load_users
import argparse
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(
        description = "Import users tool"
    )
    
    parser.add_argument("input",type=Path)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("errors.csv")
    )
    
    args = parser.parse_args(argv)
    pairs, errors = load_users(args.input)
    uniques, duplicates, conflicts = find_duplicates(pairs)
    print(f"Valid: {len(uniques)}, invalid: {len(errors)}, duplicates: {len(duplicates)}, conflicts: {len(conflicts)}")
    total = errors + duplicates + conflicts
    write_error_report(total, args.out)

from toolkit.report import write_error_report
from toolkit.dedupe import find_duplicates
from toolkit.reader import load_users
import argparse
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(
        description = "Import users tool"
    )
    
    parser.add_argument("input",type=Path)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("errors.csv")
    )
    
    args = parser.parse_args(argv)
    pairs, errors = load_users(args.input)
    uniques, duplicates, conflicts = find_duplicates(pairs)
    print(f"Valid: {len(uniques)}, invalid: {len(errors)}, duplicates: {len(duplicates)}, conflicts: {len(conflicts)}")
    total = errors + duplicates + conflicts
    write_error_report(total, args.out)

if __name__ == "__main__": main()