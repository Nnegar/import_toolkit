from toolkit.report import write_error_report
from toolkit.dedupe import find_duplicates
from toolkit.reader import load_users
import argparse
from pathlib import Path


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description = "Import users tool"
    )
    
    parser.add_argument("input",type=Path)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("errors.csv")
    )
    
    args = parser.parse_args(argv)
    try:
        pairs, errors = load_users(args.input)
    except FileNotFoundError:
        print("Error: input file not found")
        return 3
    uniques, duplicates, conflicts = find_duplicates(pairs)
    print(f"Valid: {len(uniques)}, invalid: {len(errors)}, duplicates: {len(duplicates)}, conflicts: {len(conflicts)}")
    total = errors + duplicates + conflicts
    write_error_report(total, args.out)
    if conflicts or errors:
        print("There are conflicts or errors")
        return 1
    return 0
    


if __name__ == "__main__":
    raise SystemExit(main())