def ordena(lista):
    while True:
        print("Lista atual:", lista)
        print('Escolha uma opções de ordenação:'
              '\n[ 1 ] Ordenar de forma crescente'
              '\n[ 2 ] Ordenar de forma decrescente')

        ordenar = int(input('Sua opção: '))
        if ordenar == 1:
            lista.sort()
        elif ordenar == 2:
            lista.sort(reverse=True)
        else:
            print('Digite 1 para sortear a lista de forma crescente ou 2 para sortear de formar decrescente')
        return lista






