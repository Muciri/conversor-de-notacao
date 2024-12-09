import numpy as np

class pilha_sequencial:
    #CONSTRUTOR
    def __init__(self, tamanho:int):
        self.__dados = np.full(tamanho, None)
        self.__topo = -1

    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '||'
        pilha = '|'
        for i in self.__dados[:self.__topo +1]:
            pilha += f'{i}, '
        pilha = pilha.rstrip(', ') + '|'
        return pilha
    
    def __len__(self):
        return self.__topo +1
    
    #MÉTODOS DE INSTÂNCIA
    def cheia(self):
        return self.__topo == len(self.__dados)
    
    def vazia(self):
        return self.__topo == -1
    
    def topo(self):
        if self.__dados[self.__topo] != None:
            return self.__dados[self.__topo]
        else:
            print('a pilha já está vazia')
    
    def empilha(self, carga:any):
        if not self.cheia():
            self.__topo += 1
            self.__dados[self.__topo] = carga
        else:
            print('a pilha já está cheia')
    
    def desempilha(self):
        if not self.vazia():
            self.__topo -= 1
        else:
            print('a pilha já está vazia')

    def busca_elemento(self, num:int):
        try:
            if self.__dados[num] != None:
                return self.__dados[num]
            return 'elemento não encontrado'
        except IndexError:
            print('valor fora do range')
    
    def busca_posicao(self,elemento:any):
        cont = -1
        for i in self.__dados:
            cont += 1
            if i == elemento:
                return cont
            if i == None:
                break
        return 'elemento não encontrado'