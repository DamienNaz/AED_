
def cria_dicionario():
    sequencia = input(
        "Introduza uma sequência de pares chave-valor [exemplo: Darth Vador: 42, Leia Organa: 42],"
        "separados por ':' e os pares separados por vírgula: ")
    pares = sequencia.split(",")
    dicionario = {}

    for par in pares:
        chave, valor = par.split(":")
        dicionario[chave.strip()] = valor.strip()

    return dicionario

def insere_elemento(dicionario):
    chave = input("Introduza a chave [exemplo: Bluey]: ")
    valor = input("Introduza o valor [exemplo: 9]: ")
    dicionario[chave] = valor

    return dicionario

def remove_elemento(dicionario):
    print(dicionario)

    while True:
        remover = input('Introduza uma chave do dicionário para ser removida: ')

        if remover in dicionario:
            break

        print(f"A chave '{remover}' não existe no dicionário.")

    removida = dicionario.pop(remover)

    print(f"A chave '{remover}' foi removida do dicionário.")
    print("Dicionário atualizado após a remoção:")
    print(dicionario)

    return dicionario


