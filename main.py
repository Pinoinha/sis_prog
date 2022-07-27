import sys

import montador
import dumper
import loader

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
    pass

def dump(inicio=0, fim=-1):
    dumper.le_memoria(mem_interna, inicio, fim)

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
    "clear": clear
}

if __name__ == "__main__":
    print("Interpretador de assembly v0.2")
    print("Digite h para uma lista de comandos")
    print("Pressione ^D ou ^C para sair")

    while True:
        try:
            entrada = input(">>> ").split(' ')

        except EOFError:
            print()
            sys.exit(0)

        if entrada[0] in comandos:
            comandos[entrada[0]]()
        
        else:
            print("Comando não reconhecido.")
