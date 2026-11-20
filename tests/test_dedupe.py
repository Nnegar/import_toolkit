import pytest
from toolkit.reader import load_users
from toolkit.dedupe import find_duplicates

def test_unique_records(sample_users_with_errors):
    pairs , _ = load_users(sample_users_with_errors)
    uniques , _ , _= find_duplicates(pairs)
    assert [r.email for r in uniques] == ["giulia.bianco@example.com"]
    assert "giulia.verdi@example.com" not in [r.email for r in uniques]
    assert "anna.rossi@example.com" not in [r.email for r in uniques]
    
    
def test_duplicate_lines_and_reasons(sample_users_with_errors):
    pairs , errors = load_users(sample_users_with_errors)
    _ , duplicates,_ = find_duplicates(pairs)
    assert [d.line for d in duplicates] == [4,6,7]
    assert [d.reason for d in duplicates] == ["email: giulia.verdi@example.com is duplicate of line 2",
                                              "email: anna.rossi@example.com is duplicate of line 3",
                                              "email: giulia.verdi@example.com is duplicate of line 2"]
    assert [e.line for e in errors] == [5]
    
def test_conflict_line_and_reasons(sample_users_with_errors):
    pairs , errors = load_users(sample_users_with_errors)
    _,_,conflicts = find_duplicates(pairs)
    assert [c.line for c in conflicts] == [9,10,11]
    assert [c.reason for c in conflicts] ==[
        "conflicts with line 2: role differs",
        "conflicts with line 2: first_name, role differ",
        "conflicts with line 3: role differs"
    ]
