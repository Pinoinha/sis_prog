import sys

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

def bin_to_hex(num, quiet=True):
    num_hex = hex(int(str(num), base=2))
    
    if not quiet:
        print(num_hex)
        
    return num_hex

def le_memoria(mem_interna, inicio=0, fim=-1):
    for num_linha, conteudo in enumerate(mem_interna):
        if (num_linha in range(inicio, fim))or (num_linha >= inicio and fim < 0):
            print(bin_to_hex(conteudo))
