import secrets
import json
import sys
import pathlib

def load_sheets(code_dir: str) -> list:
    sheets = list()
    files = [f for f in pathlib.Path().glob(f"{code_dir}/*.json")]
    for file in files:
        sheets.append(load_sheet(file))
    return sheets

def load_sheet(code_file: str) -> dict:
    with open(code_file, 'r', encoding='UTF8') as file:
        return json.load(file)

def pick_code(codes: dict) -> dict:
    sheet_name = codes['sheet_name']
    row_num = secrets.choice(list(codes['codes']))
    row = codes['codes'][row_num]
    col = secrets.choice(list(row))
    code = row[col]
    return dict([('sheet', sheet_name), ('row', row_num), ('col' , col), ('code', code)])

def check_code(sheets: list, row_num: str, col: str, code: str) -> dict:
    for sheet in sheets:
        row = sheet['codes'].get(row_num)
        if row is None:
            print('Invalid Row')
        else:
            stored_code = row.get(col)
            if stored_code is None:
                print('Invalid Column')
            else:
                if code == stored_code:
                    return sheet

def main(sheets_dir):
    sheets = load_sheets(sheets_dir)
    num_sheets = len(sheets)
    correct = 0
    
    for i in range(num_sheets):

        sheet = secrets.choice(sheets)
        code = pick_code(sheet)
        
        if False:
            print(f"Sheets left: {len(sheets)}")
            print(f"Sheet {code['sheet']}")
            print(f"Index {code['col']}{code['row']}")
            print(f"Code  {code['code']}")
            print()

        code_input = input(f"Guess {i+1} of {num_sheets}, what is the code for {code['col']}{code['row']}? ").upper()
        found_sheet = check_code(sheets, code['row'], code['col'], code_input)

        if found_sheet is None:
            print("Code not found in your code sheets")
        else:
            print(f"Code found in sheet wth a {secrets.choice(found_sheet['sheet_name'])} in its name!")
            correct += 1
            sheets.remove(found_sheet)

    if correct == num_sheets:
        print("You win!")
    else:
        print(f"{correct} of {num_sheets} correct, try again!")

if __name__ == "__main__":
    main(sys.argv[1])
