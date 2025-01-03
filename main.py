import secrets

LETTERS = "DEFHJLMPQRSUXYZ"

def generateCode(len: int = 8) -> str:
    symbols = LETTERS + "0123456789"
    return ''.join(secrets.choice(symbols) for i in range(len))

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

# Generate the dictionary of codes
codes = generateCodeDict(rows=40, cols=12, code_len=4)

# Format and print the codes
colum_names = printColNames(codes, gap=2)
print(colum_names)
for i in codes.keys():
    print(printRow(codes, i, gap=2))
    if i % 10 == 0 and i < len(codes):
            print()
            print(colum_names)