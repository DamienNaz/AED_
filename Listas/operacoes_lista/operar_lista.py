def criar_lista():

    numeros = input("Digite uma sequência de números separados por espaço: ").strip().split()
    lista_numeros = [float(x) for x in numeros]
    lista = [int(numero) for numero in lista_numeros]
    return lista
def maximo(lista):
    print("Lista atual:", lista)
    maximo_lista = lista[0]

    for elemento in lista:
        if elemento > maximo_lista:
            maximo_lista = elemento

    return maximo_lista

def posicao_maximo(lista):
    print("Lista atual:", lista)

    maximo_valor = lista[0]
    posicao = 0

    for x in range(1, len(lista)):
        if lista[x] >= maximo_valor:
            maximo_valor = lista[x]
            posicao = x

    return posicao

def soma(lista):
    print("Lista atual:", lista)
    soma = sum(lista)
    return soma

def media(lista):
    print("Lista atual:", lista)
    soma = sum(lista) / len(lista)
    return soma



