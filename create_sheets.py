import secrets
import json

LETTERS = "DEFHIJLMPQRSUXYZ"
NUMBERS = "0346789"
SYMBOLS = LETTERS + NUMBERS

def generateCode(len: int = 8) -> str:
    return ''.join(secrets.choice(SYMBOLS) for i in range(len))

def printColNames(c: dict, gap: int = 1, **kwargs) -> str:
    header = " " * (len(str(len(c))) + 1) 
    code_len = len(list(c[1].values())[0])
    for col in c[1].keys():
        header = header + f"{col:{' '}{'^'}{code_len + gap}}"
    return header

def printRow(c: dict, row_num: int, gap: int = 1, **kwargs) -> str:
    index_str_len = len(str(len(c)))
    seperator = " " * gap
    row = seperator.join(c[row_num][code] for code in list(c[row_num]))
    return f"{row_num:{' '}{'<'}{index_str_len}} {row} {row_num:{' '}{'>'}}"

def generateCodeDict(rows: int = 20, cols: int = 4, code_len: int = 5, **kwargs) -> dict:
    column_letters = LETTERS
    if cols > len(column_letters):
        print(f"Not enough column letters available for {cols} columns")
        exit()
    c = dict()
    for i in range(1, rows + 1):
        row = dict()
        for j in column_letters[:cols]:
            row[j] = generateCode(code_len)
        c[i] = row
    return c

def main(rows: int = 10, cols: int = 10, code_len: int = 3, print_symbols: bool = False) -> None:
    # Generate the dictionary of codes
    codes = generateCodeDict(rows=rows, cols=cols, code_len=code_len)
    sheet_name = generateCode(4)
    text_file_name = f"codes_{sheet_name}.txt"
    json_file_name = f"codes_{sheet_name}.json"
    code_file = dict([('sheet_name', sheet_name), ('codes',  codes)])
    sheet_width = len(printRow(codes, 1, gap=1)) + 1

    # Write the coes to a json file
    with open(json_file_name, 'w', encoding='utf-8') as jf:
        json.dump(code_file, jf, ensure_ascii=False, separators=(',', ':'), indent=None)

    with open(text_file_name, 'w', encoding="utf-8") as tf:
        output = tf

        # Create a sheet ID and center it at the top along with the allowed symbols
        print(f"{'  ' + sheet_name + '  ':{'*'}{'^'}{sheet_width}}"+"\n", file=output)

        if print_symbols:
            print(f"{' ' + ' '.join(sorted(SYMBOLS))\
                     + ' ':{'*'}{'^'}{sheet_width}}"+"\n", file=output)

        # Format and print the codes
        colum_names = printColNames(codes, gap=1)
        print(colum_names, file=output)
        for i in codes:
            print(printRow(codes, i, gap=1), file=output)
            if i % 10 == 0 and i < len(codes):
                print(file=output)
                print(colum_names, file=output)

        print("\n"+f"{'*' * sheet_width}", file=output)

    print(f"{text_file_name} and {json_file_name} created.")

if __name__ == "__main__":
    main()
