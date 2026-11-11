from toolkit.models import UserRecord, Role

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

