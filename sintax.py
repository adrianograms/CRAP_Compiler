
from pprint import pprint

count = 0
arguments = []
arguments_tree = []
count_args = 0
file_tree = open("tree.txt", "w")
variables = []
current_line = 0
error_count_sematic = 0
for_place = 0
for_line = []


class Variable:
    def __repr__(self):
        return str(self.__dict__)
    def __str__(self):
        return str(self.__dict__)

def print_list(buffer, tabs):
    if type(buffer) == list and len(buffer) > 1:
        tabs = tabs +  1
        for i in buffer:
            print_list(i, tabs)
    else:
        for i in range(tabs):
            print(end='\t')
        print(buffer)

def creating_tree(buffer, above):
    if type(buffer[-1]) == str:
        global count
        global count_args
        global file_tree
        count += 1
        label = '"%s"' % letter_to_symbol(buffer[-1]) 
        buffer[-1] = '"%s"' %  (letter_to_symbol(buffer[-1]) + str(count))

        text = '%s [label=%s]\n' % (buffer[-1],label) 
        file_tree.write(text)
        text = '%s -> %s\n' % (above, buffer[-1])
        file_tree.write(text)

        creating_tree(buffer[-2], buffer[-1])

        if len(buffer) > 2:
            for i in range(len(buffer)-2):
                creating_tree(buffer[i], buffer[-1])
    else:
        count_args += 1

        label = str(buffer[1])
        identifier = '"%s"' % (label + str(count_args))
        label = '"%s"' % label

        text = '%s [label=%s]\n' % (identifier, label)
        file_tree.write(text)
        text = '%s -> %s\n' % (above, identifier)
        file_tree.write(text)



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
        "$": 34,
        "i8": 35,
        "i16": 36,
        "i32": 37,
        "i64": 38,
        "u8": 39,
        "u16": 40,
        "u32": 41,
        "u64": 42,
        "f32": 43,
        "f64": 44,
        "generic": 45
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
        34: "$",
        35: "i8",
        36: "i16",
        37: "i32",
        38: "i64",
        39: "u8",
        40: "u16",
        41: "u32",
        42: "u64",
        43: "f32",
        44: "f64",
        45: "generic"
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

def letter_to_symbol(letter):
    switcher = {
        "A": "<global>",
        "B": "<numeric>",
        "C": "<array>",
        "D": "<type>",
        "E": "<expression>",
        "F": "<expressions>",
        "G": "<bool_expr>",
        "H": "<rela_expr>",
        "I": "<math_expr>",
        "J": "<expr>",
        "K": "<term>",
        "L": "<factor>",
        "M": "<if>",
        "N": "<when>",
        "O": "<for>",
        "P": "<loop>",
        "Q": "<let>",
        "R": "<assignable>",
        "T": "<assignment>",
        "U": "<array_index>",
        "V": "<read>",
        "Y": "<print>"
    }
    return switcher.get(letter)

error_list = [ "ed", "ed", "erA1", "ep21", "erE1", "erE1", "erE1", "erE1", "erE1", "erE1", "ed", "ed",
            "ed", "ed", "ed", "ep10", "erR1", "erR1", "erR1", "ed", "erF2", "erY2", "erG1", "erH1",
            "erI1", "erJ1", "erK1", "ed", "erL1", "erL1", "erL1", "ed", "ed", "erL1", "ed", "erB1",
            "erB1", "ep29", "ep7", "ep30", "ep15", "ed", "ed", "ep4", "erF3", "ed", "ed", "ed", "ed",
            "ed", "ed", "erL2", "erL2", "ed", "erD1", "erD1", "ed", "ep21", "ep21", "ep21", "ed",
            "erT3", "erT3", "erT3", "erV1", "ep3", "ed", "erG3", "erH3", "erI3", "erJ3", "erK3", "erL3", 
            "erL3", "ed", "ed", "ed", "ed", "ep31", "ed", "erU4", "erQ4", "ep3", "ep8", "ep9", "ep9",
            "ed", "erT5", "erC4", "ep21", "erN6", "erP6", "ep7", "ed", "ep21", "ep9", "ed", 
            "erM9", "ep9", "erO10"]

def print_error(line, line_aux, message):
    print(message, line_aux[0][2])
    if line != None:
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


def verify_type_variable(name):
    global variables
    for var in variables:
        if var.name == name:
            # if var.type == 'arr':
            #     return var.inside_type
            return var.type
    return None

def take_type(value, line):
    elem = value[0]
    if elem == 13:
        elem = verify_type_variable(value[1])
        #elem = token_to_number(elem)
        if elem == 'arr':
            #print("Variavel ?? um vetor, sendo preciso os '[]' para usa-la")
            print_error(None, line,"Erro Semantico: Variavel ?? um vetor. Linha:")
            elem = 45
        if elem == None:
            print_error(None, line,"Erro Semantico: Variavel n??o declarada. Linha:")
            elem = 45
    return elem

def isArray(name):
    global variables
    for var in variables:
        if var.name == name:
            if var.type == 'arr':
                return var
            else:
                #print('N??o Array')
                return None
    #print('Variavel n??o existe')
    return None

def mathComparisson(value1, value2):
    if value1 == 5 or value2 == 5:
        return False, 45
    if value1 == value2: #Tipos iguais
        return True, value1
    elif value1 == 22 and (value2 >= 35 and value2 <= 42): #Para a combin????o numeric com outro tipo inteiro
        return True, value2
    elif value2 == 22 and (value1 >= 35 and value1 <= 42):
        return True, value1
    elif value1 == 25 and value2 in [43,44]: #Para a combin????o real com outro tipo real
        return True, value2
    elif value2 == 25 and value1 in [43,44]:
        return True, value1
    elif value1 == 45 or value2 == 45: #Tipo generico
        return True, 45
    else:
        return False, 45

def boolComparisson(value1, value2):
    if value1 == value2 and value1 == 5: #Dois valores do tipo boolean
        return True, value1
    elif value1 == 45 or value2 == 45:
        return True, 45
    else:
        return False, 45

def generalComparaison(value1, value2):
    valid1, _ = mathComparisson(value1, value2)
    valid2, _ = boolComparisson(value1, value2)
    return valid1 or valid2

def popArguments(arguments, value):
    for i in range(value):
        arguments.pop(-1)

#Redu????o, verifica????o semantica e gera????o da arvore
def reduction(f, buffer, matrix, line):
    global arguments
    global arguments_tree
    global variables
    global current_line
    global error_count_sematic
    aux = f[1]
    pops = int(f[2:])
    inside = []
    # Verifica a redu????o a ser feita, e adiciona esse valor em um vetor, contendo todo o
    # conteudo relevante vindo da redu????o, e com esses dados, eles s??o encapsulados em um
    # vetor com o estado que ele representa para ser usado na arvore 
    if aux in 'RLKJIHGBEDA' and pops == 1:
        inside.append(buffer[-2])

    elif aux in 'KJIHG' and pops == 3:
        inside.append(buffer[-6])
        inside.append(buffer[-4])
        inside.append(buffer[-2])
        combine = arguments_tree[-3:]

        # Aqui s??o feitas as verifica????es semanticas do codigo, usando o estado ao qual ele foi reduzido.
        # Se utiliza um vetor de argumentos, apenas com as informa????es necessarias para a verifica????o de
        # tipos para as quest??es semanticas
        if aux == 'G':
            left = take_type(combine[0], line)
            right = take_type(combine[2], line)
            valid, type_next = boolComparisson(right, left)
            if not valid:
                # Tratamento dos erros semanticos, n??o geram falha na gera????o da arvore
                print_error(None, line, "Erro Semantico: Tipos invalidos. Linha:")
                error_count_sematic += 1
                combine.insert(0,45)
            else:
                combine.insert(0,5)

        elif aux in 'IJKH':
            left = take_type(combine[0], line)
            right = take_type(combine[2], line)
            valid, type_next = mathComparisson(left, right)
            if not valid:
                string_erro = ""
                if left != right:
                    string_erro = "Erro Semantico: Tipos %s e %s incompativeis, operando na mesma express??o. Linha:" % (number_to_token(left), number_to_token(right))
                else:
                    string_erro = "Erro Semantico: tipos invalidos na express??o. Linha:"
                print_error(None, line, string_erro)
                error_count_sematic += 1
                combine.insert(0, 45)
            else:
                if aux == 'H':
                    combine.insert(0, 5)
                else:
                    combine.insert(0, type_next)

        popArguments(arguments_tree, 3)
        arguments_tree.append(combine)

    elif aux == 'M':
        inside.append(buffer[-16])
        inside.append(buffer[-10])
        inside.append(buffer[-4])
        combine = arguments_tree[-1:]
        expr = take_type(combine[0], line)

        if not (expr in [5,45]):
            print_error(None, line, "Erro Semantico: Express??o do if invalida. Linha:")
            error_count_sematic += 1

        popArguments(arguments_tree, 1)

    elif aux == 'N':
        inside.append(buffer[-10])
        inside.append(buffer[-4])
        combine = arguments_tree[-1:]
        expr = take_type(combine[0], line)

        if not (expr in [5,45]):
            print_error(None, line, "Erro Semantico: Express??o do when invalida. Linha:")
            error_count_sematic += 1

        popArguments(arguments_tree, 1)

    elif aux == 'O':
        inside.append(buffer[-18])
        inside.append(buffer[-14])
        inside.append(buffer[-10])
        inside.append(buffer[-4])

        combine = arguments_tree[-3:]
        popArguments(arguments_tree, 3)

        global for_line

        type_i = take_type(combine[0], for_line)

        if not (type_i >= 35 and type_i <= 42):
            print_error(None, for_line, "Erro Semantico: Variavel invalida no la??o for. Linha:")
            error_count_sematic += 1

    elif aux == 'P':
        inside.append(buffer[-10])
        inside.append(buffer[-4])

    elif aux == 'Q':
        inside.append(buffer[-6])
        inside.append(buffer[-2])

        combine = arguments_tree[-2:]
        popArguments(arguments_tree, 2)

        type_v = 45

        if verify_type_variable(combine[0][1]) != None:
            print_error(None, line, "Erro Semantico: Variavel j?? declarada. Linha:")
            error_count_sematic += 1

        else:
            #Cria????o de variavel
            v = Variable()

            if(combine[1][0] == 46):
                v.type = 'arr'
                v.inside_type = token_to_number(combine[1][1][1])
                type_v = v.inside_type
                v.number = combine[1][2][1]
            else:
                v.type = token_to_number(combine[1][1])
                type_v = v.type
            v.name = combine[0][1]
            variables.append(v)

        combine.insert(0,type_v)
        arguments_tree.append(combine)
        #print(variables)
    elif aux == 'T' and pops == 3:
        inside.append(buffer[-6])
        inside.append(buffer[-4])
        inside.append(buffer[-2])

        combine = arguments_tree[-2:]

        if combine[1][0] != 24:
            left = take_type(combine[0], line)
            right = take_type(combine[1], line)
            #valid, type_next = mathComparisson(left, right)
            if right == 27:
                right = 39
            valid = generalComparaison(left, right)
            if not valid:
                print_error(None, line, "Erro Semantico: Atribui????o invalida. Linha:")
                error_count_sematic += 1
            #print(type_next)

        popArguments(arguments_tree, 2)

    elif aux == 'T' and pops == 5:
        inside.append(buffer[-10])
        inside.append(buffer[-6])
        inside.append(buffer[-2])

        combine = arguments_tree[-3:]
        popArguments(arguments_tree, 3)

        left = take_type(combine[0], line)
        right = take_type(combine[1], line)
        new_type = token_to_number(combine[2][1])

        if not (left == new_type) and left != 45:
            print_error(None, line, "Erro Semantico: Convers??o de tipos invalida. Linha:")
            error_count_sematic += 1
        else:
            combine.insert(0, left)
        #arguments_tree.append(combine)

    elif aux == 'U':
        inside.append(buffer[-8])
        inside.append(buffer[-4])
        combine =  arguments_tree[-2:]
        array = isArray(combine[0][1])
        if(array != None):
            combine.insert(0,array.inside_type)
        else:
            print_error(None, line, "Erro Semantico: Variavel n??o ?? um array. Linha:")
            error_count_sematic += 1
            combine.insert(0,45)

        type_inside = take_type(combine[2], line)
        if not ((type_inside >= 35 and type_inside <= 42) or type_inside == 22):
            print_error(None, line, "Erro Semantico: indice do vetor n??o ?? inteiro. Linha:")

        popArguments(arguments_tree, 2)
        arguments_tree.append(combine)
        #print(combine)
    elif aux == 'F' and pops == 2:
        inside.append(buffer[-4])
    elif aux == 'F' and pops == 3:
        inside.append(buffer[-2])
        inside.append(buffer[-6])
    elif aux == 'C':
        inside.append(buffer[-6])
        inside.append(buffer[-4])

        combine = [46]
        combine.extend(arguments_tree[-2:])
        popArguments(arguments_tree, 2)

        arguments_tree.append(combine)
    elif aux == 'L' and pops == 2:
        inside.append(buffer[-2])
    elif aux == 'L' and pops == 3 and buffer[-2][1] == ')':
        inside.append(buffer[-4])
    elif aux == 'L' and pops == 3:
        inside.append(buffer[-4])
        inside.append(buffer[-2])
    elif aux == 'Y':
        inside.append(buffer[-2])
        popArguments(arguments_tree, 1)
    elif aux == 'V':
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
    global arguments_tree
    global current_line
    global error_count_sematic
    global for_line
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
    print_section("Erros")
    for line in lines:  
        line_aux = line.copy()   
        while(line != [] and error <= 5):
            f = matrix[buffer[-1]][line[0][0]]
            if f == '':
                codigo = error_list[buffer[-1]]
                if codigo[1] == 'd':
                    #if error == 0:
                        #print_section("Erros")
                    print_error(line, line_aux,
                        "Erro Sintatico: token invalido na linha: ")
                    if line[0][0] in [5,6,11,13,17,19,20,22,24,25,26,27,28,32]:
                        arguments_tree.pop(-1)
                    line.pop(0)
                    error += 1
                elif codigo[1] == 'p':
                    if error == 0:
                        print_section("Erros")
                    aux = int(codigo[2:])
                    line.insert(0,[aux,number_to_token(aux),line_aux[0][2]])
                    if line[0][0] in [5,6,11,13,17,19,20,22,24,25,26,27,28,32]:
                        arguments_tree.append(line[0])
                    print_error(line, line_aux,
                        "Erro Sintatico: ausensia de token na linha: ")
                    error += 1
                elif codigo[1] == 'r':
                    f_aux = codigo[1:]
                    reduction(f_aux, buffer, matrix, line_aux)
            elif f[0] == 's':
                valid_value = [5,6,11,13,17,19,20,22,24,25,26,27,28,32]
                if(line[0][0] in valid_value):
                    arguments_tree.append(line[0])
                    current_line = line[0][2]
                if(line[0][0] == 12):
                    for_line = line_aux
                buffer.append(line[0])
                line.pop(0)
                buffer.append(int(f[1:]))
            elif f[0] == 'r' :
                reduction(f, buffer, matrix, line_aux)
            elif f[0] == 'a':
                if error >= 1:
                    print_section("Falha na sintaxe da linguagem!")
                else:
                    global file_tree
                    #pprint(buffer)
                    #print(len(buffer))
                    creating_tree(buffer[-2],'Z')
                    file_tree.close()
                    if error == 0 and error_count_sematic == 0:
                        print("Sem Erros!\n")
                    # pprint(buffer[-2])
                    #print(arguments_tree)
                    print_section("Sintaxe Correta!")
                    if error_count_sematic > 0:
                        print_section("Falha na Sematica!")
                    else:
                        print_section("Sucesso na Semantica!")
                return
                    
        if error >= 5:
            print_section("Muitas falhas na sintaxe da linguagem!")
            return

def read_txt(name):
    f = open(name, "r")
    matrix = []
    for line in f:
        line_aux = line.split(";")
        line_aux[-1] = line_aux[-1].replace("\n","")
        matrix.append(line_aux)
    return matrix
