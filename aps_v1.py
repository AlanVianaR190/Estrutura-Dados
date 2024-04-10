#metodos
def horaData():
    '''
    Metodo para mostrar hora e data
    :return: data e hora
    '''

    #importando biblioteca hora e data
    from datetime import datetime

    #
    agora = datetime.now()
    dh = agora.strftime("%d/%m/%y - %H:%M:%S")

    #
    return dh



def geradorCod(lista):
    '''
    Este metodo gera um pequeno codigo
    :param lista: verifica se este codigo ja consta em alguma lista para refazer o codigo
    :return: cod
    '''

    #importando a biblioteca escolher
    from random import randint, choice

    #
    letra = tuple(("A","B","C","D","E"))
    numero = randint(10, 99)

    #verifica se ja contem o codigo na lista
    cod = choice(letra) + str(numero)
    if cod in lista:
        cod = choice(letra) + str(numero)

    #
    return cod



def opcPers(lista):
    from time import sleep

    '''
    Um método personalizável onde se pode criar opções ou menu
    :param lista: declare uma lista com suas opções
    :return: a opção escolhida
    '''

    while True:
        # Visualizar opções
        print("O que deseja fazer: ")
        for pos, item in enumerate(lista):
            print(f"{pos+1} - {item}")
            sleep(0.5)
        print("")

        # Validação/tratamento de erro
        try:
            opcao = int(input("Digite uma das opções: "))
            if opcao >= 1 and opcao <= len(lista):
                return lista[opcao-1]
            else:
                print("ESTA OPÇÃO NÃO EXISTE!")
                print("")

        except:
            print("OPÇÃO INVÁLIDA. Digite um número.")
            print("")



def prefer():
    '''
    Um metodo de validação com duas opções
    :return: a opção escolhida
    '''

    #validação
    opcao = str(input("Atendimento preferencial [S]/[N]: ")).upper().strip()
    while opcao not in("S","N"):
        print("OPÇÃO INVALIDA!")
        opcao = str(input("Atendimento preferencial [S]/[N]: ")).upper().strip()

    #
    if opcao in("S"):
        return "SIM"
    else:
        return "NÃO"



def geraSenha(listaMotiv, lista):
    '''
    Este metodo cria um dicionario no formato de senha, utilizando outros metodos para complementar
    :param listaMotiv: uma lista com opções, este parametro utiliza do metodo <opcDepart()>
    :return: um dicionario
    '''

    #dicionario
    senha = dict()

    #utilizando metodos para criação do dicionario
    senha["SENHA"] = geradorCod(lista)
    senha["DATA & HORA"] = horaData()
    senha["MOTIVO"] = opcPers(listaMotiv)
    print("")
    senha["ATENDIMENTO PREFERENCIAL"] = prefer()
    print("")

    return senha



def ticket(dicio, txt=""):
    '''
    Este metodo vizualiza um dicionario formatado
    :param dicio: um dicionario
    :param txt: uma mensagem não obrigatoria
    :return: nada apenas vizualiza as informações de um dicionario
    '''

    #
    for campo, info in dicio.items():
        print(f"{campo}: {info}", end=" | ")
    print(txt)
    print("")



def filaSenha(lista):
    '''
    Este metodo permite vizualizar uma lista como uma fila
    :param lista: uma lista
    :return: sem return apenas vizualiza uma lista de modo formatado
    '''

    #condição caso não haja items na lista para vizualizar
    if len(lista) > 0:

        #laço para posição da lista
        for pos, item in enumerate(lista):
            print(f"{pos+1} - ",end="")

            #função para vizualizar
            ticket(item)

    #
    else:
        print("NÃO CONTEM SENHAS NA LISTA!")
        print("")



def chamaSenha(lista):
    '''
    Este metodo retira uma senha
    :param lista: uma lista
    :return: sem return, apenas vizualiza a senha chamada ou removida
    '''

    #
    if len(lista) > 0:

        #
        chamada = verifPref(lista)
        if chamada is None:
            chamada = lista.pop(0)
        ticket(chamada, "O ATENDENTE O AGUARDA!")


    else:
        print("NÃO CONTEM SENHAS NA LISTA!")
        print("")


def verifPref(lista):
    '''
    Este metodo verifica se ha preferencial SIM na lista
    :param lista: uma lista
    :return: a posição na lista onde se encontra o primeiro sim, ou nada
    '''
    #
    for pos,item in enumerate(lista):
        if item["ATENDIMENTO PREFERENCIAL"] == "SIM":
            return lista.pop(pos)
    return None


def finalSec(lista):
    if len(lista) > 0:
        print("NÃO E POSSIVEL SAIR")
        print(f"AINDA CONSTA {len(lista)} SENHAS NA LISTA PARA SER CHAMADAS!")
        print("")
        return " "
    else:
        resposta = verifSN()
        return resposta


def verifSN():

    print("Responda apenas sim[s] / não[n]...")
    resp = str(input("Deseja encerrar o programa? ")).upper().strip()[0]
    print()

    while resp not in("S","N"):
        print("Responda apenas sim[s] / não[n]...")
        resp = str(input("Deseja encerrar o programa? ")).upper().strip()[0]
        print()

    return resp


def salvarHist(lista):
    from datetime import datetime

    agora = datetime.now()
    dh = agora.strftime("%d/%m/%y-%H:%M:%S")

    with open("C:/Users/Maria/Desktop/historico_" + dh.replace("/","_").replace(":","_") + ".txt", "w") as arquivo:
        for item in lista:
            arquivo.write(str(item) + "\n")

#programa principal

#lista do programa principal
senhas = list()

##
historico = list()

#laço para validar a opção do programa principal
while True:

    #
    tupla = tuple(("GERAR SENHA","MOSTRAR FILA DE SENHAS","CHAMAR PROXIMA SENHA","SAIR"))
    opc = opcPers(tupla)

    #opção 1
    if opc in("GERAR SENHA"):

        #lista com opções
        tupla1 = tuple(("ABERTURA DE CONTA","DEPOSITO E SAQUE","PAGAMENTOS","FINANCIAMENTOS","INVESTIMENTOS"))

        #função para gerar senha
        senha = geraSenha(tupla1, senhas)

        #função para adicionar a senha na lista
        senhas.append(senha.copy())

        #função para vizualizar senha criada
        ticket(senha, "AGUARDE POR FAVOR!")

        ##
        historico.append(senha)

    #
    elif opc in("MOSTRAR FILA DE SENHAS"):

        #função para vizualizar senhas na lista/fila
        filaSenha(senhas)

    #
    elif opc in("CHAMAR PROXIMA SENHA"):

        #função para chamar senha da lista/fila
        chamaSenha(senhas)

    #
    elif opc in("SAIR"):

        sair = finalSec(senhas)
        if sair in("S"):
            break


print("PROGRAMA ENCERRADO")

#função que cria um historico das senhas geradas
salvarHist(historico)







