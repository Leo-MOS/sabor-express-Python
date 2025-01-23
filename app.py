import os #Necessário para utilizar o método que limpa o terminal

def exibir_nome_do_programa():
    print('\n### Sabor Express ###')

def exibir_opcoes():
    print('''
        1. Cadastrar restaurante
        2. Listar restaurantes
        3. Ativar restaurante
        4. Sair
        ''')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite ENTER para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida) #Esta seria uma alternativa à linha anterior

        match opcao_escolhida:
            case 1:
                print('Cadastrar restaurante')
            case 2:
                print('Cadastrar restaurante')
            case 3:
                print('Cadastrar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def finalizar_app():
    os.system('cls') #Limpa o terminal
    print('App finalizado.')

if __name__ == '__main__':
    main()