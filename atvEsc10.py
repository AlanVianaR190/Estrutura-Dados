#metodo

def verifSN(txt):
    #
    print("Responda apenas sim[s] / não[n]...")
    resp = str(input(txt)).lower().strip()[0]
    print()

    #
    while resp not in("s","n"):
        print("Responda apenas sim[s] / não[n]...")
        resp = str(input(txt)).lower().strip()[0]
    print()

    #
    return resp


#
def tabela(lista, txt = ""):
    print(f"=-=-=-=-=-=-=-=-=-=-=-= {txt} -=-=-=-=-=-=-=-=-=-=-=-=")
    for produto, valor in lista.items():
        print(f"PRODUTO: {produto}     QUANTIDADE: {valor[0]}     \tPREÇO unit: ${valor[1]:.2f}")
    print()


#
def compraClient(lista, val=0):
    print("Minha compras foram: ")
    for item in lista:
        print(f"{item['Quantidade']} {item['Produto']} por ${item['Valor']:.2f}")
    print(f"O valor total da compra foi de ${val:.2f}")
    print()


#programa
estoque = {"tomate": [1000, 2.30],"alface": [500, 0.45], "batata": [2000, 1.20],"cebola": [100, 1.50]}

#lista para armazenar os produtos do cliente
lista = list()

#variavel para valor total da compra
valTot = 0

#função p tabela de produtos
tabela(estoque)

#laço para passar por estoque de produtos
for produto, valor in estoque.items():

    #variavel com metodo para escolher se comprara o produto
    a1 = verifSN(f"Deseja comprar {produto}?")

    #
    if a1 in("s"):

        #dicionario para armazenar o produto
        item = dict()

        #o produto e adicionado ao dicionario
        item["Produto"] = produto

        #a quantidade e adicionada ao dicionario
        item["Quantidade"] = int(input("Quantos? "))
        print()

        #o valor baseado  na quantidade do produto e adicionado ao dicionario
        item["Valor"] = item["Quantidade"] * valor[1]

        #variavel para calcular o valor total da compra
        valTot += item["Valor"]

        #acrescentado o dicionario do produto na lista
        lista.append(item.copy())

        #diminuir a quantidade de produto no estoque
        valor[0] -= item["Quantidade"]

#função para mostar a lista de compra do cliente
compraClient(lista,valTot)

#função p tabela de produtos
tabela(estoque)
