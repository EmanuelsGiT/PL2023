from tpc1 import tpc1
from matplotlib import pyplot as plt

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
                elif option == 2 : 
                    table("Distribuicao por sexo", dist_sexo)
                    x = ["Masculino", "Feminino"]
                    y = list(dados.distr_sexo()[0])
                    plt.bar(x, y, color="black")
                    plt.xlabel("Género")
                    plt.ylabel("Número de pessoas com a doença")
                    plt.title("Distribuição da doença por Género")
                    plt.show()
                elif option == 3 : 
                    etario = dados.distr_etario()
                    table("Distribuicao por idade", etario)
                    x = dict(etario).keys()
                    y = dict(etario).values()
                    plt.bar(x, y, color="red")
                    plt.xlabel("Faixa Etária (anos)")
                    plt.ylabel("Número de pessoas com a doença")
                    plt.title("Distribuição da doença por Idades")
                    plt.show()
                elif option == 4 : 
                    col = dados.distr_colesterol()
                    table("Distribuicao por colesterol", col)
                    x = dict(col).keys()
                    y = dict(col).values()
                    plt.bar(x, y, color="green")
                    plt.xlabel("Nivel de colesterol")
                    plt.ylabel("Número de pessoas com a doença")
                    plt.title("Distribuição da doença por nivel de colesterol")
                    plt.show()
            else:
                print('Opção Inválida')
        else:
            print('Input Inválido')

if __name__ != "main":
    main()

h = data()
dist_sexo = h.dist_sexo()
dist_ee = h.dist_ee()
dist_nc = h.dist_nc()
table("Distribuicao por sexo", dist_sexo)
y1 = ["Masculino", "Feminino"]
y2 = list(h.dist_sexo()[0])
plt.bar(y1, y2, color="red")
plt.xlabel("Género")
plt.ylabel("Número de pessoas com a doença")
plt.title("Distribuição da doença por Género")
plt.show()

table("Distribuicao por idade", dist_ee)
y1 = dict(dist_ee).keys()
y2 = dict(dist_ee).values()
plt.bar(y1, y2, color="red")
plt.xlabel("Faixa Etária (anos)")
plt.ylabel("Número de pessoas com a doença")
plt.title("Distribuição da doença por Idades")
plt.show()

table("Distribuicao por colesterol", dist_nc)
y1 = dict(dist_nc).keys()
y2 = dict(dist_nc).values()
plt.bar(y1, y2, color="red")
plt.xlabel("Nivel de colesterol")
plt.ylabel("Número de pessoas com a doença")
plt.title("Distribuição da doença por nivel de colesterol")
plt.show()