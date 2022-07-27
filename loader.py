import sys

import montador

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

class Loader(object):
    def __init__(self, memoria, instrucoes="Intrucoes.txt"):
        self.memoria = memoria,
        self.instrucoes = instrucoes
    
    def hex_to_bin(self, num, quiet=True):
        num_bin = bin(int(str(num), base=16))
        
        if not quiet:
            print(num_bin)
            
        return num_bin
    
    def read_and_store(self):
        with open(self.instrucoes) as instru:
            for num_linha, instrução in enumerate(instru):
                # a primeira linha é *sempre* ignorada
                if num_linha == 0:
                    continue
    
                write(hex_to_bin(instrução))
    
    def write(self, dados, endereco_base=""):
        self.memoria.append(dados)
