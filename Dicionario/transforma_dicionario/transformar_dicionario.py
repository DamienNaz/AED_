def apresenta_ordenado(dicionario):
    print(f'Dicionário atual: {dicionario}')
    ordenar = dicionario
    print('Dicionário ordenado pela chave:')
    return sorted(ordenar)

def soma_valores(dicionario):
    print(f'Dicionário atual: {dicionario}')
    soma = 0
    for valor in dicionario.values():
        soma += int(valor)
    return soma

def media_valores(dicionario):
    print(f'Dicionário atual: {dicionario}')
    valores = 0
    for valor in dicionario.values():
        valores += int(valor)
    total = float(len(dicionario))
    media = valores / total
    return media

def maximo_valores(dicionario):
    print(f'Dicionário atual: {dicionario}')
    valor_maximo = None
    for valor in dicionario.values():
        valor_inteiro = int(valor)
        if valor_maximo is None or valor_inteiro > valor_maximo:
            valor_maximo = valor_inteiro
    return valor_maximo


