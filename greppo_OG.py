import argparse
import sys
import re


def search_file(filename, search_strings, show_line_numbers=False, invert_match=False):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, 1):
                for search_string in search_strings:
                    if re.search(search_string, line):
                        if invert_match:
                            break
                        result = filename
                        if show_line_numbers:
                            result += f':{line_number}'
                        result += f':{line.strip()}'
                        print(result)
                        return True
    except FileNotFoundError:
        print(f"greppo.py: {filename}: File not found", file=sys.stderr)
        return False
    return False


def main():
    parser = argparse.ArgumentParser(description='Search for text strings in files.')
    parser.add_argument('filenames', metavar='filename', nargs='+', help='One or more filenames')
    parser.add_argument('--search', '-s', action='append', dest='search_strings', required=True,
                        help='Search string(s) to look for')
    parser.add_argument('-n', '--line-number', action='store_true', help='Display line numbers')
    parser.add_argument('-v', '--invert-match', action='store_true', help='Invert the sense of matching')
    parser.add_argument('-q', '--quiet', '--silent', action='store_true', help='Suppress all normal output')
    
    args = parser.parse_args()

    search_strings = args.search_strings
    show_line_numbers = args.line_number
    invert_match = args.invert_match
    quiet = args.quiet

    found_match = False
    for filename in args.filenames:
        if search_file(filename, search_strings, show_line_numbers, invert_match):
            found_match = True

    if found_match:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()