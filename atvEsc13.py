#metodos
def verifSN(txt):

    print("Responda apenas sim[s] / não[n]...")
    resp = str(input(txt)).lower().strip()[0]
    print()

    while resp not in("s","n"):
        print("Responda apenas sim[s] / não[n]...")
        resp = str(input(txt)).lower().strip()[0]
        print()

    return resp


def menuEscolh():

    tupla = tuple(("Criar", "Ler", "Atualizar", "Apagar", "Sair"))

    for i, item in enumerate(tupla):
        print(i+1 , item)

    opc = int(input("Digite uma opção: "))

    return opc


def criarCad():

    dicionario = dict()

    '''A função capitalize() formata o primeiro caracter para maiuscula'''
    dicionario["NOME"] = str(input("Digite o nome: ")).strip().capitalize()

    dicionario["TELEFONE"] = int(input("Digite o telefone: "))

    print("Contato criado!")

    return dicionario


def lerCad(lista):

    import operator

    '''key é um argumento que pode ser passado para a função sorted() ou outras funções de ordenação
    em Python. Essa chave especifica uma função de um argumento que é usada para extrair um valor que é então
    usado para ordenar os elementos.'''
    listaOrdenada = sorted(lista, key=operator.itemgetter("NOME"))

    for dicionario in listaOrdenada:

        print(dicionario["NOME"], dicionario["TELEFONE"])
        print()


def atualizCad(lista):

    busca = str(input("Digite o nome: ")).strip().capitalize()

    for dicionario in lista:

        if dicionario["NOME"] in(busca):

            nome = str(input("Digite o nome: ")).strip().capitalize()
            dicionario["NOME"] = nome

            telefone = int(input("Digite o telefone: "))
            dicionario["TELEFONE"] = telefone

    print("Contato atualizado!")


def excluiCad(lista):

    busca = str(input("Digite o nome: ")).strip().capitalize()

    for num, dicionario in enumerate(lista):

        if dicionario["NOME"] in(busca):

            lista.pop(num)

    print("Contato excluido!")

#programa principal
lista = list()

while True:

    opcao = menuEscolh()
    print()

    if opcao == 1:

        criar = criarCad()
        print()

        lista.append(criar.copy())

    elif opcao == 2:

        lerCad(lista)
        print()

    elif opcao == 3:

        atualizCad(lista)
        print()

    elif opcao == 4:

        excluiCad(lista)
        print()

    elif opcao ==5:
        print("Programa encerado!")
        break

    else:
        print("Opção invalida!")
        print()




