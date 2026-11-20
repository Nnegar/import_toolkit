import pytest

@pytest.fixture
def sample_users_with_errors(tmp_path):
    path = tmp_path/"duplicate_users.csv"
    path.write_text(
        "email,first_name,last_name,role\n"
        "giulia.verdi@example.com,Giulia,Verdi,viewer\n"
        "  anna.rossi@example.com  ,Anna,Rossi,admin\n"
        "giulia.verdi@example.com,Giulia,Verdi,viewer\n"
        "sara.costa@example.com,Sara,Costa,superuser\n"
        "Anna.Rossi@example.com  ,Anna,Rossi, Admin\n"
        "giulia.verdi@example.com,Giulia,Verdi,viewer\n"
        "giulia.bianco@example.com,Giulia,Bianco,viewer\n"
        "giulia.verdi@example.com,Giulia,Verdi,Admin\n"
        "giulia.verdi@example.com,Giuly,Verdi,analyst\n"
        "anna.rossi@example.com,Anna,Rossi,viewer"
    )
    return path