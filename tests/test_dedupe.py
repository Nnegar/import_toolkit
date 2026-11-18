import pytest
from toolkit.reader import load_users
from toolkit.dedupe import find_duplicates

@pytest.fixture
def sample_duplicate_user(tmp_path):
    path = tmp_path/"duplicate_users.csv"
    path.write_text(
        "email,first_name,last_name,role\n"
        "giulia.verdi@example.com,Giulia,Verdi,viewer\n"
        "  anna.rossi@example.com  ,Anna,Rossi,admin\n"
        "giulia.verdi@example.com,Giulia,Verdi,viewer\n"
        "sara.costa@example.com,Sara,Costa,superuser\n"
        "Anna.Rossi@example.com  ,Anna,Rossi, Admin\n"
    )
    return path



def test_unique_records(sample_duplicate_user):
    pairs , _ = load_users(sample_duplicate_user)
    #find_duplicates > tuple[list[UserRecord], list[RowError]]
    uniques , _ = find_duplicates(pairs)
    assert len(uniques) == 2
    
    
def test_duplicate_lines_and_reasons(sample_duplicate_user):
    pairs , errors = load_users(sample_duplicate_user)
    _ , duplicates = find_duplicates(pairs)
    assert [d.line for d in duplicates] == [4,6]
    assert [d.reason for d in duplicates] == ["email: giulia.verdi@example.com is duplicate of line 2",
                                              "email: anna.rossi@example.com is duplicate of line 3"]
    assert len(errors)==1
    