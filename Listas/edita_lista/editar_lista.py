def criar_lista():

    numeros = input("Digite uma sequência de números separados por espaço: ").strip().split()
    lista_numeros = [float(x) for x in numeros]
    lista = [int(numero) for numero in lista_numeros]
    return lista

def acrescenta_elemento(lista):
    try:
        numero = float(input("Digite um número para adicionar à lista: "))
        lista.append(int(numero))
    except ValueError:
        print("Digite um número válido.")
    return lista

def insere_elemento(lista):

    while True:
        print("Lista atual:", lista)
        posicao = int(input("Digite a posição onde deseja inserir o elemento: "))

        if posicao < 0 or posicao > len(lista)+1:
            print(f"Posição inválida, deverá colocar um número entre 0 e {len(lista)+1} ")
        else:
            break

    valor = float(input("Digite o valor a ser inserido: "))
    valor = int(valor)
    lista.insert(posicao, valor)
    print("Elemento inserido com sucesso.")

def remove_de_indice(lista):
    while True:
        print("Lista atual:", lista)
        posicao = int(input("Digite a posição onde deseja remover o elemento: "))

        if posicao < 0 or posicao >= len(lista):
            print(f"Posição inválida, deve ser um número entre 0 e {len(lista) - 1}.")
        else:
            break


    remover = lista.pop(posicao)
    print(f"O elemento {remover} foi removido com sucesso.")
    return lista

def remove_elemento(lista):
    while True:
        print("Lista atual:", lista)
        elemento = int(input("Digite o elemento que deseja remover da lista: "))

        if elemento in lista:
            lista.remove(elemento)
            print(f"O elemento {elemento} foi removido com sucesso.")
            break
        else:
            print(f"O elemento {elemento} não existe na lista, tente novamente.")
    return lista

def ordena(lista):
    while True:
        print("Lista atual:", lista)
        ordenar = int(input('Se pretende ordenar a lista de forma crescente digite 1 \n'
                        'Se pretende ordenar a lista de forma decrescente digite 2: '))
        if ordenar == 1:
            lista.sort()
        elif ordenar == 2:
            lista.sort(reverse=True)
        else:
            print('Digite 1 para sortear a lista de forma crescente ou 2 para sortear de formar decrescente')
        return lista


def maximo(lista):
    print("Lista atual:", lista)
    maximo_lista = lista[0]

    for elemento in lista:
        if elemento > maximo_lista:
            maximo_lista = elemento

    return maximo_lista


