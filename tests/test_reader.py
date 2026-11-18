import pytest
from toolkit.reader import load_users


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path/"users.csv"
    path.write_text(
        "email,first_name,last_name,role\n"
        "anna.rossi@example.com,Anna,Rossi,admin\n"
        "  Marco.Bianchi@Example.com ,Marco,Bianchi,analyst\n"
        "giulia.verdi@example,Giulia,Verdi,viewer\n"
        "luca.neri@example.com,,Neri,viewer\n"
        "sara.costa@example.com,Sara,Costa,superuser\n"
        "paolo.gallo@example.com,Paolo,Gallo,Viewer\n"
        "elena.fontana@example.com,Elena,Fontana,analyst\n"
    )
    return path


def test_load_users_counts_and_lines(sample_csv):
    pairs, errors = load_users(sample_csv)
    assert len(errors) == 3
    assert len(pairs) == 4
    assert [e.line for e in errors] == [4,5,6]
    assert [line for line,_ in pairs] == [2,3,7,8]
    
