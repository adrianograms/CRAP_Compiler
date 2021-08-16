
from pprint import pprint

def print_list(buffer, tabs):
    if type(buffer) == list and len(buffer) > 1:
        tabs = tabs +  1
        for i in buffer:
            print_list(i, tabs)
    else:
        for i in range(tabs):
            print(end='\t')
        print(buffer)

def creating_tree(buffer, number, above):
    if type(buffer[-1]) == str and buffer[-1] != 'Y' and buffer[-1] != 'V':
        print("hello")
        number += 1
        print(above, number,'->',buffer[-1], number+1)
        creating_tree(buffer[-2], number, buffer[-1])
        if len(buffer) > 2:
            for i in range(len(buffer)-2):
                creating_tree(buffer[i], number, buffer[-1])
    else:
        print(buffer)


def token_to_number(argument):
    switcher = {
        "invalid": -1,
        "(": 0,
        ")": 1,
        "[": 2,
        "]": 3,
        "as": 4,
        "bool": 5,
        "bool_operators": 6,
        "do": 7,
        "else": 8,
        "end": 9,
        "equal": 10,
        "expr_operator": 11,
        "for": 12,
        "identifier": 13,
        "if": 14,
        "in": 15,
        "let": 16,
        "logic_unary": 17,
        "loop": 18,
        "math_operators": 19,
        "math_unary": 20,
        "newline": 21,
        "number": 22,
        "print": 23,
        "read": 24,
        "real": 25,
        "relation_operators": 26,
        "string": 27,
        "term_operator": 28,
        "then": 29,
        "times": 30,
        "to": 31,
        "type": 32,
        "when": 33,
        "$": 34
    }
    return switcher.get(argument,-1)

def number_to_token(argument):
    switcher = {
        0: "(",
        1: ")",
        2: "[",
        3: "]",
        4: "as",
        5: "bool",
        6: "bool_operators",
        7: "do",
        8: "else",
        9: "end",
        10: "=",
        11: "expr_operator",
        12: "for",
        13: "identifier",
        14: "if",
        15: "in",
        16: "let",
        17: "logic_unary",
        18: "loop",
        19: "math_operators",
        20: "math_unary",
        21: "\n",
        22: "number",
        23: "print",
        24: "read",
        25: "real",
        26: "relation_operators",
        27: "string",
        28: "term_operator",
        29: "then",
        30: "times",
        31: "to",
        32: "type",
        33: "when",
        34: "$"
    }
    return switcher.get(argument,-1)

def letter_to_number(letter):
    switcher = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "Y": 22
    }
    return switcher.get(letter)

error_list = [ "ed", "ed", "erA1", "ep21", "erE1", "erE1", "erE1", "erE1", "erE1", "erE1", "ed", "ed",
            "ed", "ed", "ed", "ep10", "erR1", "erR1", "erR1", "ed", "erF2", "erY2", "erG1", "erH1",
            "erI1", "erJ1", "erK1", "ed", "erL1", "erL1", "erL1", "ed", "ed", "erL1", "ed", "erB1",
            "erB1", "ed", "ed", "ep29", "ep15", "ed", "ed", "ep4", "erF3", "ed", "ed", "ed", "ed",
            "ed", "ed", "erL2", "erL2", "ed", "erD1", "erD1", "ed", "ep21", "ep21", "ep21", "ed",
            "erT3", "erT3", "erT3", "erV1", "ep3", "ed", "erG3", "erH3", "erI3", "erJ3", "erK3", "erL3", 
            "erL3", "ed", "ed", "ed", "ed", "ep31", "ed", "erU4", "erQ4", "ep3", "ep8", "ep9", "ep9",
            "ed", "erT5", "erC4", "ep21", "erN6", "erP6", "ep7", "ed", "ep21", "ep9", "ed", 
            "erM9", "ep9", "erO10"]

def print_error(line, line_aux, message):
    print(message, line_aux[0][2])
    print("Token: ", end='')
    if line[0][1] == '\n':
        print("newline")
    elif line[0][1] == "keyword":
        print(number_to_token(line[0][0]))
    else:
        print(line[0][1])
    print("Linha: ", end='')
    for token in line_aux:
        if token[1] == 'keyword':
            print(number_to_token(token[0]), end=' ')
        elif token[1] == '\n':
            print(token[1], end='')
        else:
            print(token[1], end=' ')
    print('\n')

def print_section(name):
    separator = '-'*len(name)
    print(separator)
    print(name)
    print(separator)
    print('\n')

def reduction(f, buffer, matrix):
    aux = f[1]
    pops = int(f[2:])
    inside = []
    if (aux == 'R' or aux == 'L' or aux == 'K' or aux == 'J' or aux == 'I' or aux == 'H' or aux == 'G' or aux == 'B' or aux =='E' or aux == 'D' or aux == 'A') and pops == 1:
        # print(buffer[len(buffer)-2])
        # content = buffer[-2]
        # if aux == 'R' or aux == 'L' or aux == 'B':
        #     if type(content[-1]) == str:
        #         content = content.pop(-1)
        # inside.append(content)
        inside.append(buffer[-2])
    elif (aux == 'K' or aux == 'J' or aux == 'I' or aux == 'H' or aux == 'G') and pops == 3:
        inside.append(buffer[-6])
        inside.append(buffer[-4])
        inside.append(buffer[-2])
    elif aux == 'M':
        inside.append(buffer[-16])
        inside.append(buffer[-10])
        inside.append(buffer[-4])
    elif aux == 'N':
        inside.append(buffer[-10])
        inside.append(buffer[-4])
    elif aux == 'O':
        inside.append(buffer[-18])
        inside.append(buffer[-14])
        inside.append(buffer[-10])
        inside.append(buffer[-4])
    elif aux == 'P':
        inside.append(buffer[-10])
        inside.append(buffer[-4])
    elif aux == 'Q':
        inside.append(buffer[-6])
        inside.append(buffer[-2])
    elif aux == 'T' and pops == 3:
        # inside = buffer[-6]
        inside.append(buffer[-6])
        inside.append(buffer[-2])
        # print(inside[0], "=", inside[1])
    elif aux == 'T' and pops == 5:
        inside.append(buffer[-10])
        inside.append(buffer[-6])
        inside.append(buffer[-2])
    elif aux == 'U':
        inside.append(buffer[-8])
        inside.append(buffer[-4])
    elif aux == 'F' and pops == 2:
        inside.append(buffer[-4])
    elif aux == 'F' and pops == 3:
        inside.append(buffer[-2])
        inside.append(buffer[-6])
    elif aux == 'C':
        inside.append(buffer[-6])
        inside.append(buffer[-4])
    elif aux == 'L' and pops == 2:
        inside.append(buffer[-2])
    elif aux == 'L' and pops == 3 and buffer[-2][1] == ')':
        inside.append(buffer[-4])
    elif aux == 'L' and pops == 3:
        inside.append(buffer[-4])
        inside.append(buffer[-2])

    # for i in inside:
    #     if type(i) != str and type(i[-1]) == str:
    #         i.pop(-1) 

    #if aux == 'Y':
        #pprint(buffer)
    for i in range(pops*2):
        buffer.pop(len(buffer)-1)
    row = buffer[-1]
    inside.append(aux)
    buffer.append(inside)
    column = letter_to_number(buffer[-1][-1]) + 34
    if matrix[row][column] == '':
        print_section("Erro grave!")
        return
    buffer.append(int(matrix[row][column]))

def sintax(tokens):
    matrix = read_txt("tabela.txt")
    buffer = [0]
    #print(tokens)
    for token in tokens:
        token[0] = token_to_number(token[0])
    lines = []
    line = []
    i = 0
    for token in tokens:
        if(token[0] == -1):
            continue
        if token[2] != i:
            lines.append(line)
            line = [token]
            i = token[2]
        else:
            line.append(token)
    line.append([34,"$"])
    lines.append(line)
    error = 0
    for line in lines:  
        line_aux = line.copy()   
        while(line != [] and error <= 5):
            f = matrix[buffer[-1]][line[0][0]]
            if f == '':
                codigo = error_list[buffer[-1]]
                if codigo[1] == 'd':
                    if error == 0:
                        print_section("Erros")
                    print_error(line, line_aux,
                        "Erro, token invalido na linha: ")
                    line.pop(0)
                    error += 1
                elif codigo[1] == 'p':
                    if error == 0:
                        print_section("Erros")
                    aux = int(codigo[2:])
                    line.insert(0,[aux,number_to_token(aux),line_aux[0][2]])
                    print_error(line, line_aux,
                        "Erro, ausensia de token na linha: ")
                    error += 1
                elif codigo[1] == 'r':
                    f_aux = codigo[1:]
                    reduction(f_aux, buffer, matrix)
            elif f[0] == 's':
                buffer.append(line[0])
                line.pop(0)
                buffer.append(int(f[1:]))
            elif f[0] == 'r' :
                reduction(f, buffer, matrix)
            elif f[0] == 'a':
                if error >= 1:
                    print_section("Falha na sintaxe da linguagem!")
                else:
                    pprint(buffer)
                    print(len(buffer))
                    creating_tree(buffer[-2],0,'Z')
                    # pprint(buffer[-2])
                    print_section("Sintaxe Correta!")
                return
                    
        if error >= 5:
            print_section("Falha na sintaxe da linguagem!")
            return

def read_txt(name):
    f = open(name, "r")
    matrix = []
    for line in f:
        line_aux = line.split(";")
        line_aux[-1] = line_aux[-1].replace("\n","")
        matrix.append(line_aux)
    return matrix
