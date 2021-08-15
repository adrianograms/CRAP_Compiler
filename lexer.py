INIT    = 0
COMMENT = 1
WORD    = 2
INTEGER = 3
REAL    = 4
OP      = 5
TYPE    = 6
STRING  = 7

def peek(src, i, fn):
    return i + 1 < len(src) and fn(src[i + 1])

def is_char(c):
    return ord(c) >= 97 and ord(c) < 123

def is_number(c):
    return ord(c) >= 48 and ord(c) < 58

def is_op(c):
    return c in ['=', '!', '+', '-', '*', '/', '%', '&', '|', '~', '^', '<', '>']

def is_whitespace(c):
    return c == '\t' or c == ' '

def lexer(src):
    line = 1

    buf = []
    ret = []

    state = INIT

    p = None
    i = 0

    while i < len(src):

        if len(ret) > 0:
            p = ret[-1]
        
        c = src[i]

        if state == INIT:
            if (c == '\n'):
                if p is not None and not p[0] == 'newline':
                    ret.append(['newline', '\n', line])
                buf = []
                line += 1

            elif is_whitespace(c):
                pass

            elif is_char(c):
                if peek(src, i, is_number):
                    state = TYPE
                else:
                    state = WORD
                buf.append(c)

            elif is_op(c):
                state = OP
                buf.append(c)

            elif c == '#':
                state = COMMENT

            elif c == '(' or c == ')' or c == '[' or c == ']':
                ret.append([c, c, line])

            elif is_number(c):
                state = INTEGER
                buf.append(c)

            elif c == '"':
                state = STRING

            else:
                ret.append(['invalid', c, line])
                buf = []

        elif state == COMMENT:
            if c == '\n':
               state = INIT
               i -= 1

        elif state == WORD:
            if is_char(c):
                buf.append(c)
            else:
                state = INIT

                buf = ''.join(buf)

                if buf == 'bool':
                    ret.append(['type', 'bool', line])

                elif buf in ['true', 'false']:
                    ret.append(['bool', buf, line])

                elif buf == 'not':
                    ret.append(['logic_unary', 'not', line])

                elif buf in ['and', 'or']:
                    ret.append(['bool_operators', buf, line])

                elif buf in ['as', 'do', 'let', 'if', 'then', 'else', 'for', 'in', 'loop', 'times', 'end', 'when', 'read', 'print', 'to']:
                    ret.append([buf, 'keyword', line])

                else:
                    ret.append(['identifier', buf, line])

                state = INIT
                buf = []
                i -= 1

        elif state == INTEGER:
            if c == '.':
                state = REAL
                buf.append(c)

            elif is_number(c):
                buf.append(c)

            else:
                state = INIT
                ret.append(['number', ''.join(buf), line])
                buf = []
                i -= 1

        elif state == REAL:
            if is_number(c):
                buf.append(c)

            else:
                state = INIT
                ret.append(['real', ''.join(buf), line])
                buf = []
                i -= 1

        elif state == OP:
            if (c == '=' and (src[i - 1] in ['!', '=', '<', '>'])) or (c == '<' and src[i - 1] == '<') or (c == '>' and src[i - 1] == '='):
                buf.append(c)
            else:
                i -= 1

            op_type = 'invalid_operator'

            buf = ''.join(buf)

            if buf in ['-', '~']:
                if buf == '-' and p[0] in ['(', 'math_unary', 'math_operator', 'expr_operator', 'term_operator', 'relation_operators', 'equal', 'print']:
                    op_type = 'math_unary'
                else:
                    op_type = 'expr_operator'

            elif buf in ['|', '&', '^' , '<<', '>>']:
                op_type = 'math_operator'

            elif buf == '+':
                op_type = 'expr_operator'

            elif buf in ['*', '/', '%']:
                op_type = 'term_operator'

            elif buf in ['<', '>', '<=', '>=', '==', '!=']:
                op_type = 'relation_operators'

            elif buf == '=':
                op_type = 'equal'

            state = INIT
            ret.append([op_type, buf, line])
            buf = []

        elif state == TYPE:
            if is_number(c):
                buf.append(c)
            else:
                buf = ''.join(buf)
                if buf in ['i8', 'i16', 'i32', 'i64', 'u8', 'u16', 'u32', 'u64', 'f32', 'f64']:
                    ret.append(['type', buf, line])
                else:
                    ret.append(['invalid_type', buf, line])

                state = INIT
                buf = []
                i -= 1

        elif state == STRING:
            if c == '"':
                state = INIT
                ret.append(['string', ''.join(buf), line])
                buf = []
            else:
                buf.append(c)

        i += 1
    return ret
