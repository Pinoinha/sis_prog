import sys

if __name__ == "__main__":
    print("Este arquivo é um módulo. Não execute-o.")
    sys.exit(1)

traduções = {
    "JUMP": {
        "código": "0x0",
        "instrução": "Desvio incondicional",
        "tamanho": 2
    },
    "JUMP0": {
        "código": "0x1",
        "instrução": "Desvio se zero",
        "tamanho": 2
    },
    "JUMPN": {
        "código": "0x2",
        "instrução": "Desvio se negativo",
        "tamanho": 2
    },
    "ADD": {
        "código": "0x3",
        "instrução": "Soma",
        "tamanho": 2
    },
    "SUB": {
        "código": "0x4",
        "instrução": "Subtração",
        "tamanho": 2
    },
    "MUL": {
        "código": "0x5",
        "instrução": "Multiplicação",
        "tamanho": 2
    },
    "DIV": {
        "código": "0x6",
        "instrução": "Divisão",
        "tamanho": 2
    },
    "LOAD": {
        "código": "0x7",
        "instrução": "Carregar acumulador",
        "tamanho": 2
    },
    "STORE": {
        "código": "0x8",
        "instrução": "Guardar na memória",
        "tamanho": 2
    },
    "CALL": {
        "código": ("0x9", "0xA", "0xB"),
        "instrução": "Chamar subrotina",
        "tamanho": 2
    },
    "RTN": {
        "código": "0xC",
        "instrução": "Retorno de subrotina",
        "tamanho": 1
    },
    "STOP": {
        "código": "0xD",
        "instrução": "Parar o programa",
        "tamanho": 1
    },
    "READ": {
        "código": "0xE",
        "instrução": "Ler um byte da fita para o acumulador",
        "tamanho": 1
    },
    "WRITE": {
        "código": "0xF",
        "instrução": "Perfurar fita com byte do acumulador",
        "tamanho": 1
    }
}

def traduzir(mnemonico):
    # se o mnemonico não estiver no dicionário, é porque já está em hex
    if traduções.get(mnemonico) is not None:
        return traduções.get(mnemonico).get("código")
    return mnemonico
    #return traduções.get(mnemonico).get("código") or mnemonico
