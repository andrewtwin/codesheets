import secrets
import json
import sys

def load_sheet(code_file: str) -> dict:
    with open(code_file, 'r', encoding='UTF8') as file:
        return json.load(file)

def pick_code(codes: dict) -> dict:
    sheet_name = codes['sheet_name']
    row_num = secrets.choice(list(codes['codes']))
    row = codes['codes'][row_num]
    col = secrets.choice(list(row))
    code = row[col]
    return dict([('sheet', sheet_name), ('index', f"{col}{row_num}"), ('code', code)])

def main(sheet_name):
    codes = load_sheet(sheet_name)
    code = pick_code(codes)
    print(f"Sheet {code['sheet']}")
    print(f"Index {code['index']}")
    print(f"Code  {code['code']}")

if __name__ == "__main__":
    main(sheet_name = sys.argv[1])