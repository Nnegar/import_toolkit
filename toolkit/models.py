from enum import Enum
from dataclasses import dataclass
import re

class Role(str, Enum):
    ADMIN = "admin"
    ANALYST = "analyst"
    VIEWER = "viewer"
    
    
@dataclass(frozen=True)
class UserRecord:
    email: str
    first_name : str
    last_name: str
    role : Role
    
    def __post_init__(self):
        #checks the email pattern. it should start with a-z A-z numbers + or -
        #one or more charachters then a dot then the same pattern but no + this time 
        #then another dot and zero to two other alphabet charachters
        if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", self.email) is None:
            raise ValueError(f"email: invalid format {self.email!r}")
        
        if self.first_name == "":
            raise ValueError("first_name: empty")
        
        if self.last_name == "":
            raise ValueError("last_name: empty")
        
        if not isinstance(self.role, Role):
            raise ValueError(f"role: not a role {self.role!r}")
            
        
