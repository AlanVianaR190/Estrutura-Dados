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


def status(lista):
    #
    pontos = 0

    #
    for resposta in lista:
        if resposta in("s"):
            pontos += 1

    #
    if pontos <2:
        return "Inocente"
    elif pontos == 2:
        return "Suspeita"
    elif pontos >2 and pontos <=4:
        return "Cumplice"
    else:
        return "Assasino"



def perguntas():

    respostas = list()

    a = verifSN("Telefonou para a vítima?")
    respostas.append(a)
    b = verifSN("Esteve no local do crime?")
    respostas.append(b)
    c = verifSN("Mora perto da vitima?")
    respostas.append(c)
    d = verifSN("Devia para a vitima?")
    respostas.append(d)
    e = verifSN("Já trabalhou com a vitima?")
    respostas.append(e)

    return status(respostas)


#programa

#
classif = perguntas()
print(f"De acordo com respostas esta pessoa e considerada(o): {classif}")

