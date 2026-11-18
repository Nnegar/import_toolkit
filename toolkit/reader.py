from toolkit.models import UserRecord, Role
from dataclasses import dataclass
import csv


@dataclass
class RowError:
    line: int
    reason: str


def parse_row(row: dict) -> UserRecord:
    email = row["email"].strip().lower()
    first_name = row["first_name"].strip()
    last_name = row["last_name"].strip()
    role = row["role"].strip().lower()
    try:
        role = Role(role)
    except ValueError:
        #I added from None in order to not show two identical 
        #error message. this way it only shows this one
        #and not the one fro the original Role class
        raise ValueError(f"role: unknown value {role!r}") from None
            
    return UserRecord(email=email, first_name=first_name,
                      last_name=last_name, role=role)
    
    
def load_users(path) -> tuple[list[tuple[int, UserRecord]],list[RowError]]:
    pairs = []
    errors = []
    with open(path, newline="",encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        #DictReader consumes the header, so the first data row is file line 2.
        for row_num, row in enumerate(reader, start = 2):
            try:
                pairs.append((row_num, parse_row(row)))
            except ValueError as error:
                errors.append(RowError(line=row_num,reason=str(error)))
                
    return pairs, errors
    



    