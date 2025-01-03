import secrets

LETTERS = "DEFHJLMPQRSUXYZ"
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
    return f"{row_num:{' '}{'<'}{index_str_len}} {row} {row_num}"

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

def main() -> None:
    # Generate the dictionary of codes
    codes = generateCodeDict(rows=4, cols=10, code_len=4)

    # Create a sheet ID and center it at the top along with the allowed symbols
    sheetWidth = len(printRow(codes, 1, gap=2))
    print(f"{'  ' + generateCode(8) + '  ':{'*'}{'^'}{sheetWidth}}"+"\n")
    print(f"{" ".join(sorted(SYMBOLS)):{' '}{'^'}{sheetWidth}}"+"\n")

    # Format and print the codes
    colum_names = printColNames(codes, gap=2)
    print(colum_names)
    for i in codes.keys():
        print(printRow(codes, i, gap=2))
        if i % 10 == 0 and i < len(codes):
                print()
                print(colum_names)


if __name__ == "__main__":
    main()