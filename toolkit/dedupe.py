from toolkit.reader import RowError
from toolkit.models import UserRecord
from dataclasses import  fields


def find_duplicates(rows: list[tuple[int, UserRecord]]) -> tuple[list[UserRecord], list[RowError], list[RowError]]:
    duplicates=[]
    conflicted=[]
    conflicted_emails=set()
    unique = []
    seen={}
    for line, record in rows:
        if record.email in seen:
            has_conf,confs=has_conflict(seen[record.email][1], record)
            if has_conf:
                conflicted.append(RowError(line=line,reason=f"conflicts with line {seen[record.email][0]}: {", ".join(confs)} differ{'s' if len(confs) == 1 else ''}"))
                conflicted_emails.add(record.email)
            else:   
                duplicates.append(RowError(line=line,reason=f"email: {record.email} is duplicate of line {seen[record.email][0]}"))
        else:
            seen[record.email]=(line, record)
            unique.append(record)
    kept = [r for r in unique if r.email not in conflicted_emails]
    
    return kept, duplicates, conflicted
            
        
        
        
def has_conflict(record1: UserRecord,record2: UserRecord) -> tuple[bool,list]:
    conflicts=[]
    for f in fields(record1):
        if not getattr(record1, f.name) == getattr(record2,f.name):
            conflicts.append(f.name)
    return bool(conflicts), conflicts

    
