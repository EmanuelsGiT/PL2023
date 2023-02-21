from tpc1 import tpc1

def main():
    dados = tpc1()
    file = 'myheart.csv'
    #file = input('Insira o nome do ficheiro: ')
    print('A ler dados do ficheiro ' + file)
    dados.parserFile(file)
    print('Dados lidos')
    option = 0
    while option != 5:
        print('Menu:')
        print('1 - Tabela dados')
        print('2 - Distribuição por sexo')
        print('3 - Distribuição por escalões etários')
        print('4 - Distribuição por níveis de colestrol')
        print('5 - Sair')
        op = input('Escolha uma opção:')
        if op.isdigit():
            option = int(op)
            if option > 0 and option < 6:
                if option == 1: print(dados)
                elif option == 2 : dados.distr_sexo()
                elif option == 3 : dados.distr_etario()
                elif option == 4 : dados.distr_colesterol()
            else:
                print('Opção Inválida')
        else:
            print('Input Inválido')

if __name__ != "main":
    main()
