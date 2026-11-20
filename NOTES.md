line 2: valid
line 3: valid after .strip() and .lower()
line 4: invalid, domain has no dot.
line 5: invalid, first name is empty
line 6: invalid, unknown role
line 7: valid after clean up, role.lowercase
line 8: valid



desision for separating dedup from loaduser or not: I separate it because it can be scaled, easier to debug and test and change


email,first_name,last_name,role
giulia.verdi@example.com,Giulia,Verdi,viewer
anna.rossi@example.com,Anna,Rossi,admin
giulia.verdi@example.com,Giulia,Verdi,viewer
sara.costa@example.com,Sara,Costa,superuser
  Anna.Rossi@example.com  ,Anna,Rossi, Admin

line 2: valid
line 3: valid
line 4: duplicate of line 2
line 5: invalid
line 6: duplicate of line 3

2 valid, 2 duplicate and 1 error
enumerate


Line 2("giulia.verdi@example.com,Giulia,Verdi,viewer\n"): valid
line 3("  anna.rossi@example.com  ,Anna,Rossi,admin\n"): valid
Line 4("giulia.verdi@example.com,Giulia,Verdi,viewer\n"): invalid>duplicate of line 2
line 5("sara.costa@example.com,Sara,Costa,superuser\n"): invalid>wrong role
Line 6("Anna.Rossi@example.com  ,Anna,Rossi, Admin\n"): invalid> duplicate of line 3
line 7("giulia.bianco@example.com,Giulia,Bianco,viewer\n"): valid
Line 9("giulia.verdi@example.com,Giulia,Verdi,Admin\n"): invalid>conflict with line 2. 
line 10("giulia.verdi@example.com,Giuly,Verdi,analyst\n"):invalid>conflict with line 2

