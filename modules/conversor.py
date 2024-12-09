from modules.pilha_sequencial import pilha_sequencial
from modules.aritmetic import *

def converte_posfixa(expressão):
    exp = expressão.replace(' ', '')
    pilha = pilha_sequencial(len(exp))
    saida = ''
    
    for i in exp:
        if e_operando(i):
            saida += i
        
        elif e_operador(i) and pilha.vazia():
            pilha.empilha(i)
        
        elif e_operador(i) and not pilha.vazia():
            if prioridade(pilha.topo()) >= prioridade(i):
                saida += pilha.topo()
                pilha.desempilha()
            pilha.empilha(i)
        
        elif i == '(':
            pilha.empilha(i)

        elif i == ')' and not pilha.vazia():
            while pilha.topo() != '(':
                saida += pilha.topo()
                pilha.desempilha()
            pilha.desempilha()

        else:
            pass

    while not pilha.vazia():
        saida += pilha.topo()
        pilha.desempilha()
    
    return saida