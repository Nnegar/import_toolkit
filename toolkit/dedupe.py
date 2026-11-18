from toolkit.reader import RowError
from toolkit.models import UserRecord


def find_duplicates(rows: list[tuple[int, UserRecord]]) -> tuple[list[UserRecord], list[RowError]]:
    duplicates=[]
    unique = []
    seen={}
    for line, record in rows:
        if record.email in seen:
            duplicates.append(RowError(line=line,reason=f"email: {record.email} is duplicate of line {seen[record.email]}"))
        else:
            seen[record.email]=line
            unique.append(record)
    return unique, duplicates
            
        

    
