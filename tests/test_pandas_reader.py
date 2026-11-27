from toolkit.pandas_reader import load_users_df


def test_line_numbers(sample_users_with_errors):
    df = load_users_df(sample_users_with_errors)
    assert df["line"].tolist() == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_cleaning(tmp_path):
    path = tmp_path / "users.csv"
    path.write_text(
                "email,first_name,last_name,role\n"
                "Giulia.Verdi@example.com,Giulia  ,Verdi, viewer\n"
                "  anna.rossi@example.com  ,  Anna, RoSsi,ADMIN \n"
    )
    df = load_users_df(path)
    assert df["email"].tolist() == ["giulia.verdi@example.com","anna.rossi@example.com"]
    assert df["first_name"].tolist() == ["Giulia","Anna"]
    assert df["last_name"].tolist() == ["Verdi","RoSsi"]
    assert df["role"].tolist() == ["viewer","admin"]
    
def test_empty_cell(tmp_path):
    path = tmp_path / "users.csv"
    path.write_text(
                "email,first_name,last_name,role\n"
                "Giulia.Verdi@example.com,Giulia  ,, viewer\n"
    )
    df = load_users_df(path)
    assert df["last_name"].tolist() == [""]