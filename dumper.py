import sys

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

def bin_to_hex(num, quiet=True):
    num_hex = hex(int(str(num), base=2))
    
    if not quiet:
        print(num_hex)
        
    return num_hex

def le_arquivo(arquivo, inicio=0, fim=-1):
    with open(arquivo) as memoria:
        for num_linha, conteudo in memoria:
            if num_linha in range(inicio, fim):
                print(bin_to_hex(linha))
