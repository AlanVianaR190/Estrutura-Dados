def cadAluno():
    '''
    Metodo para cadastrar alunos
    :return: um cadastro, pode ser vizualizado ou acrescentado em uma lista
    '''
    #dicionario p cadastrar aluno & lista para cadastrar notas do aluno
    aluno = dict()
    notas = list()

    #
    aluno["Nome"] = str(input("Digite o nome do aluno: ")).strip().upper()

    #acrescentar as notas na lista
    p1 = float(input("Digite a nota da primeira prova:  "))
    notas.append(p1)
    p2 = float(input("Digite a nota da segunda prova: "))
    notas.append(p2)

    #acrescentar a lista de notas no dicionario
    aluno["Notas"] = notas

    #metodo de vizualizar cadastro
    vizuCad(aluno)

    return aluno


def vizuCad(dicio):
    '''
    Metodo para vizualizar um cadastro criado
    :param dicio: acrescentar um dicionario
    :return: nda
    '''
    for key, value in dicio.items():
        print(key, value)


def calcMedSla(lista):
    '''
    Metodo para calcular media
    :param lista: acrescentar uma lista
    :return: nda
    '''
    medias = list()

    for item in lista:
        media = sum(item["Notas"]) / len(item["Notas"])
        medias.append(media)

    medSla = sum(medias) / len(medias)
    print(f"A media da sala e de: {medSla:.2f}")
    print()


def calcMedProv(lista):
    '''
    Metodo para calcular a media de ambas as provas
    :param lista: acrescentar uma lista
    :return: nda
    '''
    notasP1 = list()
    notasP2 = list()

    '''o loop externo percore cada  aluno enquanto o interno percore cada nota
    a numeração e usada junto com a condição de que se for par ira para lista x, se não ira para y '''
    for item in lista:
        for i, n1 in enumerate(item["Notas"]):
            if i % 2 == 0:
                notasP1.append(n1)
            else:
                notasP2.append(n1)

    medP1 = sum(notasP1) / len(notasP1)
    medP2 = sum(notasP2) / len(notasP2)

    print(f"Desempenho P1: {medP1:.2f} | Desempenho P2: {medP2:.2f}")
    print()


def verifSN(txt):
    '''
    Metodo de verificação se a resposta e sim, não ou esta incorreta
    :param txt: acrescentar um enunciado
    :return: a resposta selecionada
    '''
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


def vizuList(lista):
    '''
    Metodo que vizualiza uma lista com numeração
    :param lista:
    :return:
    '''
    for i, item in enumerate(lista):
        print(f"{i+1} - Aluno: {item['Nome']} ---------- Notas: {item['Notas']}")
    print()



#
#lista de alunos
alunos = list()

#contador
cont = 0

#laço para cadastrar alunos
while cont < 2:
    aluno = cadAluno()

    #acrescentar a copia de aluno na lista de alunos
    alunos.append(aluno.copy())
    print()

    #
    cont += 1

#
calcMedSla(alunos)

#
calcMedProv(alunos)

#
opc = verifSN("Deseja verificar as notas da prova? [s]/[n]")

#
if opc in("N"):
    print("Programa Encerado")
else:
    vizuList(alunos)
    print("Programa Encerado")
