import secrets
import json
import sys
import pathlib
import random
import time

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
                
def redact_name(name: str, clear_letters:int = 1, redact_char: str = "*") -> str:
    if clear_letters >= len(name):
        return name
    else:
        redacted_name = list(redact_char * len(name))
        letters_in_clear = 0
        while letters_in_clear < clear_letters:
            letter = secrets.choice(range(len(name)))
            if redacted_name[letter] == redact_char:
                redacted_name[letter] = name[letter]
                letters_in_clear += 1

        return (''.join(char  for char in redacted_name))

def main(sheets_dir):
    sheets = load_sheets(sheets_dir)
    num_sheets = len(sheets)
    random.shuffle(sheets)   
    correct = 0
    
    for i in range(num_sheets):

        sheet = sheets[0]
        code = pick_code(sheet)

        show_codes = True 
        if show_codes:
            print(f"Sheets left: {len(sheets)}")
            print(f"Sheet {code['sheet']}")
            print(f"Index {code['col']}{code['row']}")
            print(f"Code  {code['code']}")
            print()

        code_input = input(f"{num_sheets - i} guesses remain. {len(sheets)} sheets still to verify.\nInput a code at {code['col']}{code['row']}? ").upper()
        found_sheet = check_code(sheets, code['row'], code['col'], code_input)

        suspense = False
        if suspense:
            for j in range(4):
                msg = "Checking" + "." * j
                print(msg, end="\r")
                time.sleep((0.30 * i) + 0.25)

        if found_sheet is None:
            print("\n\n!!! Code not found! Session ended. !!!\n")
            break
        else:
            print(f"\n\n*** Code found! {found_sheet['sheet_name']} verified and removed for remaning guesses this turn. ***\n")
            correct += 1
            sheets.remove(found_sheet)

    if correct == num_sheets:
        win_message = ("*" * 10 + " You win! " + "*" * 10)
        print("*" * len(win_message))
        print(win_message)
        print("*" * len(win_message))
    else:
        print(f"{correct} of {num_sheets} correct; try again!")
        print("Sheets not verified:")
        print("\n".join(redact_name(sheet['sheet_name'], 1) for sheet in sheets))

if __name__ == "__main__":
    main(sys.argv[1])
