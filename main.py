import sys

import montador
import dumper
import loader
import processador

## type: usuário pode digitar assembly livremente na memória interna do programa
# mount: chama o montador no arquivo especificado e traduz assembly para hexadecimal
# run: roda o arquivo, enviando-o ao processador (processador é interno ao programa)

def _help():
    print("help, h - Mostra a lista de comandos disponíveis e suas ações")
    print("info, i - Alterna a visibilidade dos elementos de memória e registrador")
    print("dump [inicio, fim]  - Mostra a região de memória de [inicio] a [fim]. Por padrão, inicio = 0 e fim = final do arquivo")
    print("load [arquivo] - Carrega as intruções presentes em [arquivo], por padrão Instrucoes.txt")
    print("data [arquivo] - Carrega os dados presentes em [arquivo], por padrão Dados.txt")
    print("type [endereço] - Habilita a escrita na memória a partir de [endereço]")
    print("mount [fonte] [alvo] - Traduz as intruções em [fonte] e salva em [alvo]. Por padrão, [alvo] = Montado.txt")
    print("run [endereço] [-s] - Executa o programa escrito a partir de [endereço]. Caso o usuário inclua a opção -s, o programa será executado passo a passo.")
    print("clear [mem/reg/all] - Limpa o conteúdo da memória/acumulador/ambos")

def info():
    global quiet 
    quiet = not quiet

def dump(inicio=0, fim=999):
    global memoria_instrucoes
    dumper.le_memoria(memoria_instrucoes, inicio, fim)

def load(arquivo_de_instrucoes="Instrucoes.txt"):
    global memoria_instrucoes
    global quiet
    loader.read_and_store(memoria_instrucoes, arquivo_de_instrucoes, quiet)

# TODO: a função deve chamar o loader para salvar na memória interna?
def data(arquivo_de_dados="Dados.txt"):
    global memoria_dados
    global quiet

def type(endereco):
    pass

def mount(fonte="Instrucoes.txt", alvo="Montado.txt"):
    with open(alvo, 'w') as montado:
        with open(fonte) as arq:
            for linha in arq:
                if '--' not in linha:
                    hexa = montador.traduzir(str(linha).strip('\r\n'))
                    montado.write(hexa + '\n')

def run():
    processador.run()

def clear():
    memoria_instrucoes.clear()

def exit():
    sys.exit(0)

comandos = {
    "help": _help,
    "h": _help,
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
    
    memoria_instrucoes = []
    memoria_dados = []
    
    while True:
        try:
            comando, *argumentos = input(">>> ").split(' ')
        except (EOFError, KeyboardInterrupt):
            print()
            exit()

        if comando in comandos:
            try:
                comandos[comando](*argumentos)
            except TypeError:
                comandos[comando]()
        else:
            print("Comando não reconhecido.")
