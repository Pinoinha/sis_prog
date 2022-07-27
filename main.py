import sys

import montador
import dumper
from loader import Loader

# TODO: criar um vetor "memória" interno ao programa

# info: imprime, para cada operação realizada, o conteúdo do registrador; "verbose global"
# dump: imprime o que está no memoria.txt entre as linhas especificadas
# load: carrega os dados binários de um arquivo (pode ser o memoria.txt) no vetor interno "memória"
# type: usuário pode digitar assembly livremente na memória interna do programa
# mount: chama o montador no arquivo especificado e traduz assembly para hexadecimal
# run: roda o arquivo, enviando-o ao processador (processador é interno ao programa)
# clear: coloca uma string vazia

def help():
    print("help, h - Mostra a lista de comandos disponíveis e suas ações")
    print("info, i - Alterna a visibilidade dos elementos de memória e registrador")
    print("dump [inicio, fim]  - Mostra a região de memória de [inicio] a [fim]. Por padrão, inicio = 0 e fim = final do arquivo")
    print("load [arquivo] - Carrega os dados presentes em [arquivo]")
    print("type [endereço] - Habilita a escrita na memória a partir de [endereço]")
    print("mount [fonte] [alvo] - Traduz a linguagem de máquina em [fonte] e salva em [alvo]. Por padrão, [alvo] = m_[arquivo]")
    print("run [endereço] [-s] - Executa o programa escrito a partir de [endereço]. Caso o usuário inclua a opção -s, o programa será executado passo a passo.")
    print("clear [mem/reg/all] - Limpa o conteúdo da memória/acumulador/ambos")

def info():
    global quiet 
    quiet = not quiet

def dump(inicio=0, fim=-1):
    global memoria
    dumper.le_memoria(memoria, inicio, fim)

def load(arquivo_de_instrucoes="Instrucoes.txt"):
    loader = Loader(memoria, arquivo_de_instrucoes)
    loader.read_and_store(quiet)

def type(endereco):
    pass

def mount():
    pass

def run():
    pass

def clear():
    pass

def exit():
    sys.exit(0)

comandos = {
    "help": help,
    "h": help,
    "info": info,
    "i": info,
    "dump": dump,
    "load": load,
    "type": type,
    "mount": mount,
    "run": run,
    "clear": clear,
    "exit" : exit
}

quiet = True

if __name__ == "__main__":
    print("Interpretador de assembly v0.2")
    print("Digite h para uma lista de comandos")
    print("Pressione ^D ou ^C para sair")
    
    memoria = {}
      
    while True:
        try:
            entrada = input(">>> ").split(' ')

        except EOFError:
            print()
            exit()

        if entrada[0] in comandos:
            comandos[entrada[0]]()
        
        else:
            print("Comando não reconhecido.")
