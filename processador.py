import sys

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

instruções = {
    "0x0": {
        "função" : jump,
        "tamanho": 2
    },
    "0x1": {
        "função" : jump_zero,
        "tamanho": 2
    },
    "0x2": {
        "função" : jump_neg,
        "tamanho": 2
    },
    "0x3": {
        "função" : add,
        "tamanho": 2
    },
    "0x4": {
        "função" : sub,
        "tamanho": 2
    },
    "0x5": {
        "função" : mul,
        "tamanho": 2
    },
    "0x6": {
        "função" : div,
        "tamanho": 2
    },
    "0x7": {
        "função" : load,
        "tamanho": 2
    },
    "0x8": {
        "função" : store,
        "tamanho": 2
    },
    "0x9": {
        "função" : call_subr,
        "tamanho": 2
    },
    "0xC": {
        "função" : return_subr,
        "tamanho": 1
    },
    "0xD": {
        "função" : stop,
        "tamanho": 1
    }
}



def jump (valor):
    proximo_PC = valor

def jump_zero (valor):
    if acumulador == 0:
        jump(valor)

def jump_neg (valor):
    if acumulador < 0:
        jump(valor)

def add(acumulador, valor):
    acumulador += valor

def sub(acumulador, valor):
    add(acumulador, -1*valor)

def mul(acumulador, valor):
    acumulador = acumulador * valor

def div(acumulador, valor):
    acumulador = int(acumulador/valor)

def load (valor)
    #acumulador = dados[valor]
    pass

def store (valor)
    #dados[valor] = acumulador
    pass

def call_subr (valor):
    retorno_PC = atual_PC + 1
    jump(valor)

def return_subr(placeholder) :
    proximo_PC = retorno_PC

def stop(placeholder):
    running = False

running = False
atual_PC = 0
proximo_PC = 0
retorno_PC = 0

def run():
    running = True
    
    while(running):
        argumento = 0
        #cod_instrucao = memoria_instrucoes[atual_PC]
        #if (instruções.get(cod_instrucao).get("tamanho") == 1:
        #   proximo_PC = atual_PC + 1
        #else:
        #   argumento = memoria_instrucoes[atual_PC + 1]
        #   proximo_PC = atual_PC + 2
        #if cod_instrucao in instruções:
        #   try:
        #       instruções.get(cod_instrucao).get("função")(argumento)
        #except:
        #   tratamento de erro
        #else:
        #   running = False
        #   print("Texto-programa com códigos de instrução corrompidos. Verifique novamente. Execução abortada."

    pass
