#função
def apagarNome(lista):
    nomes = lista
    for nome in nomes:
        print(nome)
    print(f"\nExiste {len(nomes)} nomes na lista")

    excluir = str(input("Qual nome que deseja apagar: ")).upper().strip()
    nomes.remove(excluir)

    for nome in nomes:
        print(nome)
    print(f"\nExiste {len(nomes)} nomes na lista")


#programa
nomes = list()
cont=5

while cont>0:
    nome = str(input("Digite um nome: ")).upper()
    nomes.append(nome)
    cont-=1

#chamar função
apagarNome(nomes)
