from modules.conversor import converte_posfixa

while True:
    user = input('O que deseja fazer? \n[1] converter expressão \n[2] avaliar resultado da expressão \n[3] sair \n->')
    match user:
        case '1':
            expressao = input('digite a expressão: \n->')
            print(converte_posfixa(expressao))
        case '2':
            #todo
            pass
        case '3':
            break
        case _:
            print('resposta inválida')
