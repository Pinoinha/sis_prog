import sys

import montador

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

def hex_to_bin(num, quiet=True):
    num_hex = montador.traduzir(num)
    num_bin = bin(int(str(num_hex), base=16))
    
    if not quiet:
        print(num_bin)
        
    return num_bin

def write(memoria, dados):
    memoria.append(dados)

def read_and_store(memoria, arquivo="Montado.txt", quiet=True):
    with open(arquivo) as instru:
        for instrução in instru:
            instrução = str(instrução).strip('\r\n')     
            # linhas com '--' são consideradas comentários, e portanto ignoradas
            if '--' not in instrução:
                write(memoria, hex_to_bin(instrução, quiet))
