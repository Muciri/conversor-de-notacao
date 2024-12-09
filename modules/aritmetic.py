def prioridade(op):
    if op == '(':
        return 1
    elif op == '+' or op == '-':
        return 2
    elif op == '*' or op == '/':
        return 3
    elif op == '^':
        return 4
    else:
        return 0

def e_operando(sim):
    return sim.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def e_operador(sim):
    return sim in '+-*/^'