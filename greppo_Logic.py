#Denna funktion tar in söktermer, filnamn, flaggor för att invertera matchning och visa radnummer. 
#Den returnerar en exitkod och en lista med matchande rader enligt specifikationen.
#greppo_logic tar in söktermer, filnamn, flaggor för att invertera matchning och visa radnummer. 
#Den returnerar en exitkod (0 om en match hittades, annars 1) och en lista med matchande rader.
import sys
import re

def greppo_logic(search_terms, filenames, invert_match, show_linenumbers):
    matches = []
    exit_code = 1

    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, 1):
                    match = False
                    for search_term in search_terms:
                        if re.search(search_term, line):
                            match = True
                            break
                    if (invert_match and not match) or (not invert_match and match):
                        if show_linenumbers:
                            matches.append(f"{filename}:{line_number}:{line.strip()}")
                        else:
                            matches.append(f"{filename}:{line.strip()}")
                        exit_code = 0
        except FileNotFoundError:
            pass  # Ignore missing files

    return exit_code, matches

# Exempel på användning:
exit_code, matches = greppo_logic(["one", "two"], ["filnamn1"], False, False)
print(exit_code, matches)

exit_code, matches = greppo_logic(["o"], ["filnamn1"], False, False)
print(exit_code, matches)

exit_code, matches = greppo_logic(["o"], ["filnamn2"], False, True)
print(exit_code, matches)

exit_code, matches = greppo_logic(["e"], ["filnamn1", "filnamn2"], True, True)
print(exit_code, matches)

exit_code, matches = greppo_logic(["flower"], ["filnamn1", "filnamn2"], False, True)
print(exit_code, matches)