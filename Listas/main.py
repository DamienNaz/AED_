from edita_lista import editar_lista
from operacoes_lista import operar_lista
from transforma_lista import transformar_lista

def main():
    minha_lista = []

    while True:
        print("\n" + "*" * 25)
        print("*      Menu Principal     *")
        print("*" * 25)
        print("1. Criar Lista")
        print("2. Acrescentar Elemento")
        print("3. Inserir Elemento")
        print("4. Remover de Índice")
        print("5. Remover Elemento")
        print("6. Ordenar Lista")
        print("7. Encontrar Elemento Máximo")
        print("8. Encontrar a Posição do Máximo")
        print("9. Calcular a Soma")
        print("10. Calcular a Média")
        print("0. Sair")
        print("*" * 25)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            minha_lista = editar_lista.criar_lista()
        elif opcao == '2':
            editar_lista.acrescenta_elemento(minha_lista)
        elif opcao == '3':
            editar_lista.insere_elemento(minha_lista)
        elif opcao == '4':
            editar_lista.remove_de_indice(minha_lista)
        elif opcao == '5':
            editar_lista.remove_elemento(minha_lista)
        elif opcao == '6':
            editar_lista.ordena(minha_lista)
        elif opcao == '7':
            resultado_maximo = operar_lista.maximo(minha_lista)
            print("Número máximo da lista:", resultado_maximo)
        elif opcao == '8':
            resultado_posicao_maximo = operar_lista.posicao_maximo(minha_lista)
            print("Posição do número máximo:", resultado_posicao_maximo)
        elif opcao == '9':
            resultado_soma = operar_lista.soma(minha_lista)
            print("Soma da lista:", resultado_soma)
        elif opcao == '10':
            resultado_media = operar_lista.media(minha_lista)
            print("Média da lista:", resultado_media)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()