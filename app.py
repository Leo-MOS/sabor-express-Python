import os #Necessário para utilizar o método que limpa o terminal

lista_restaurantes = [{'nome': 'Boom Confeitaria', 'categoria': 'Confeitaria', 'ativo': True},{'nome': 'GastroBurg', 'categoria': 'Hamburgueria', 'ativo': False}]

def voltar_ao_menu():
    input('\nDigite ENTER para voltar ao menu principal')
    main() #reinicia o aplicativo

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
    print('Opção inválida!')
    voltar_ao_menu()

def exibir_subtitulo(txt):
    os.system('cls')
    print(f'### {txt} ###\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input('Digite a categoria do restaurante: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    lista_restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_restaurante} ({categoria_restaurante}) foi cadastrado com sucesso!\n')
    
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados')

    for restaurante in lista_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}')

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida) #Esta seria uma alternativa à linha anterior    

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls') #limpa o terminal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def finalizar_app():
    os.system('cls') #Limpa o terminal
    print('App finalizado.')

if __name__ == '__main__':
    main()