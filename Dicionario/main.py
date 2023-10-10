from edita_dicionario import editar_dicionario
from transforma_dicionario import transformar_dicionario

def main():
    dicionario = editar_dicionario.cria_dicionario()

    while True:
        print("Menu:\n"
              "1. Criar dicionário\n"
              "2. Inserir elemento\n"
              "3. Remover elemento\n"
              "4. Apresentar ordenado\n"
              "5. Soma dos valores\n"
              "6. Média dos valores\n"
              "7. Máximo valor\n"
              "0. Sair")

        opcao = input("Introduza a opção: ")

        if opcao == "1":
            dicionario = editar_dicionario.cria_dicionario()
        elif opcao == "2":
            dicionario = editar_dicionario.insere_elemento(dicionario)
        elif opcao == "3":
            dicionario = editar_dicionario.remove_elemento(dicionario)
        elif opcao == "4":
            print(transformar_dicionario.apresenta_ordenado(dicionario))
        elif opcao == "5":
            print(transformar_dicionario.soma_valores(dicionario))
        elif opcao == "6":
            print(transformar_dicionario.media_valores(dicionario))
        elif opcao == "7":
            print(transformar_dicionario.maximo_valores(dicionario))
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
