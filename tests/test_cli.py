from toolkit.__main__ import main
import csv
import pytest

def test_rejectet_rows_return_1(sample_users_with_errors, tmp_path):
    code = main([str(sample_users_with_errors),
                 "--out",
                 str(tmp_path / "errors.csv")])
    assert code == 1
    with open(str(tmp_path / "errors.csv"),"r") as f:
        reader = csv.DictReader(f)
        assert list(reader) == [
        {"line": "4", "reason": "email: giulia.verdi@example.com is duplicate of line 2"},
        {"line": "5", "reason": "role: unknown value 'superuser'"},
        {"line": "6", "reason": "email: anna.rossi@example.com is duplicate of line 3"},
        {"line": "7", "reason": "email: giulia.verdi@example.com is duplicate of line 2"},
        {"line": "9", "reason": "conflicts with line 2: role differs"},
        {"line": "10", "reason": "conflicts with line 2: first_name, role differ"},
        {"line": "11", "reason": "conflicts with line 3: role differs"},
    ]
        
        
def test_clean_file_returns_0(tmp_path):
    input_path = tmp_path / "users.csv"
    output_path = tmp_path / "errors.csv"
    
    input_path.write_text(
        "email,first_name,last_name,role\n"
        "giulia.verdi@example.com,Giulia,Verdi,viewer\n"
        "giulia.bianco@example.com,Giulia,Bianco,viewer\n",
        encoding="utf-8"
    )
    
    code = main([str(input_path), "--out", str(output_path)])
    assert code == 0
    assert output_path.exists()
    
def test_no_argument():
    with pytest.raises(SystemExit) as e:
        main([])
    assert e.value.code == 2