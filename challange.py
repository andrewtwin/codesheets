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
                
def redact_name(name: str, redact_char: str = "*", clear_letters:int = 1) -> str:
    redacted_name = list(redact_char * len(name))
    letters_in_clear = 0
    while letters_in_clear < clear_letters:
        letter = secrets.choice(range(len(name)))
        if redacted_name[letter] == "*":
            redacted_name[letter] = name[letter]
            letters_in_clear += 1

    return (''.join(char  for char in redacted_name))

def main(sheets_dir):
    sheets = load_sheets(sheets_dir)
    num_sheets = len(sheets)
    correct = 0
    
    for i in range(num_sheets):

        sheet = secrets.choice(sheets)
        code = pick_code(sheet)
        
        if True:
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
            print(f"Code found! Sheet removed for remaning guesses.")
            correct += 1
            sheets.remove(found_sheet)

    if correct == num_sheets:
        print("You win!")
    else:
        print(f"{correct} of {num_sheets} correct, try again!")
        print("Missing sheets:")
        print("\n".join(redact_name(sheet['sheet_name']) for sheet in sheets))

if __name__ == "__main__":
    main(sys.argv[1])
