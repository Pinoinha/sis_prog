import sys

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

def bin_to_hex(num, quiet=True):
    try:
        num_hex = hex(int(str(num), base=2))
    except ValueError:
        return hex(int(num, base=16))
    
    if not quiet:
        print(num_hex)
        
    return num_hex

def le_memoria(mem_interna, inicio=0, fim=999):
    for num_linha, conteudo in enumerate(mem_interna):
        if (num_linha in range(int(inicio), int(fim)+1)) or (num_linha >= int(inicio) and int(fim)+1 < 0):
            if '-' in conteudo:
                num_linha -= 1
            else:
                print(num_linha,'-',bin_to_hex(conteudo))
