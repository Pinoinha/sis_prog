import sys

import montador

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

def hex_to_bin(num, quiet=True):
    num_bin = bin(int(str(num), base=16))
    
    if not quiet:
        print(num_bin)
        
    return num_bin

def write(memoria, dados, endereco_base=""):
    memoria.append(dados)

def read_and_store(memoria, intrucoes="Intrucoes.txt", quiet=True):
    with open(instrucoes) as instru:
        for num_linha, instrução in enumerate(instru):
            # a primeira linha é *sempre* ignorada
            if num_linha == 0:
                continue

            write(hex_to_bin(memoria, instrução, quiet))
