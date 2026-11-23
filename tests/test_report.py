import pytest
from toolkit.reader import load_users
from toolkit.dedupe import find_duplicates
from toolkit.report import write_error_report
import csv
    
    
def test_writer(sample_users_with_errors,tmp_path):
    pairs, errors = load_users(sample_users_with_errors)
    _, duplicates,conflicts = find_duplicates(pairs)
    total = errors + duplicates + conflicts
    out = tmp_path/"errors.csv"
    write_error_report(total,out )
    with open(out, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        assert rows == [
        {"line": "5", "reason": "email: giulia.verdi@example.com is duplicate of line 2"},
        {"line": "5", "reason": "role: unknown value 'superuser'"},
        {"line": "6", "reason": "email: anna.rossi@example.com is duplicate of line 3"},
        {"line": "7", "reason": "email: giulia.verdi@example.com is duplicate of line 2"},
        {"line": "9", "reason": "conflicts with line 2: role differs"},
        {"line": "10", "reason": "conflicts with line 2: first_name, role differ"},
        {"line": "11", "reason": "conflicts with line 3: role differs"},
    ]
        
    
    
    