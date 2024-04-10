#função
def organizaNomes(lista):
    lista.sort()
    return lista


def buscaNome(lista):
    n_lista = [i for i in organizaNomes(lista)]
    print(n_lista)
    busca = int(input("Digite o numero que deseja: "))
    while busca > len(n_lista):
        print("Não existe")
        busca = int(input("Digite o numero que deseja: "))
    return n_lista[busca]



#programa
nomes = list()
cont=5

while cont>0:
    nome = str(input("Digite um nome: "))
    nomes.append(nome)
    cont-=1

#chamada função
print(buscaNome(nomes))
