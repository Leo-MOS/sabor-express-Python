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

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida) #Esta seria uma alternativa à linha anterior

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 3:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 4: #na solução original do curso os instrutores usaram else, mas assim o programa executaria o código qualquer que fosse a entrada, desde que diferente das anteriores. Prefiro retornar um erro
        finalizar_app()
    # Uma opção para a mensagem de erro seria colocar tudo dentro de uma estrutura de repetição, mas ainda não sei como fazer isso.

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def finalizar_app():
    os.system('cls') #Limpa o terminal
    print('App finalizado.')

if __name__ == '__main__':
    main()