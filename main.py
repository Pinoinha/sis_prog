import sys
import fire

import montador
import dumper

# info: imprime, para cada operação realizada, o conteúdo do registrador; "verbose global"
# dump: imprime o que está no memoria.txt entre as linhas especificadas
# load: carrega os dados binários de um arquivo (pode ser o memoria.txt) no vetor interno "memória"
# TODO: criar um vetor "memória" interno ao programa
# type: usuário pode digitar assembly livremente na memória interna do programa
# mount: chama o montador no arquivo especificado e traduz assembly para hexadecimal
# run: roda o arquivo, enviando-o ao processador (processador é interno ao programa)
# clear: coloca uma string vazia

def help():
    print("help, h - Mostra a lista de comandos disponíveis e suas ações")
    print("info, i - Alterna a visibilidade dos elementos de memória e registrador")
    print("dump [-inicio, -fim]  - Mostra a região de memória de [inicio] a [fim]. Por padrão, inicio = 0 e fim = final do arquivo")
    print("load [arquivo] - Carrega os dados presentes em [arquivo]")
    print("type [endereço] - Habilita a escrita na memória a partir de [endereço]")
    print("mount [fonte] [alvo] - Traduz a linguagem de máquina em [fonte] e salva em [alvo]. Por padrão, [alvo] = m_[arquivo]")
    print("run [endereço] [-s] - Executa o programa escrito a partir de [endereço]. Caso o usuário inclua a opção -s, o programa será executado passo a passo.")
    print("clear [mem/reg/all] - Limpa o conteúdo da memória/acumulador/ambos")

def info():
    pass

def dump(arquivo="Memoria.txt", inicio=0, fim=-1):
    dumper.le_arquivo(arquivo, inicio, fim)

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
    print("Interpretador de assembly v0.1")
    print("Digite h para uma lista de comandos")
    print("Pressione ^D para sair")

    while True:
        try:
            comando = input(">>> ")

        except EOFError:
            print()
            sys.exit(0)

        if comando in comandos:
            comandos[comando]()
        
        else:
            print("Comando não reconhecido.")
