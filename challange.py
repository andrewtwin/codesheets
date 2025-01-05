import secrets
import json
import sys

def load_sheet(code_file: str) -> dict:
    with open(code_file, 'r') as file:
        return json.load(file)
    
def main(sheet_name):
    codes = load_sheet(sheet_name)
    row_num = secrets.choice(list(codes['codes']))
    row = codes['codes'][row_num]
    col = secrets.choice(list(row))
    print(f"Sheet {codes['sheet_name']}")
    print(f"Index {col}{row_num}")
    print(f"Code  {row[col]}")

if __name__ == "__main__":
    main(sheet_name = sys.argv[1])