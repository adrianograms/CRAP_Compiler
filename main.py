import sys
from lexer import *
from sintax import *

def main(file, flags):
    with open(file) as f:
        src = f.read()

    tokens = lexer(src)

    if "-pl" in flags:
        for token in tokens:
            print(f'{file}:{token[2]} {token[1]} - {token[0]}')
        print('\n')

    sintax(tokens)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1],sys.argv[1:])
    else:
        print('no file name')
