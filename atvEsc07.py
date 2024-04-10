def nomeDoVelho():
    import numpy

    nome = numpy.empty(3,dtype="<U48")

    idade = numpy.empty(3, dtype="int32")

    nomevelho = ""
    idadevelho = 0

    for cont in range(3):
        nome[cont] = str(input("Digite o nome: "))
        idade[cont] = int(input("Digite a idade: "))


        if idade[cont] == 0 or idade[cont] > idadevelho:
            idadevelho = idade[cont]
            nomevelho = nome[cont]


    print(f"O mais velho e {nomevelho} com {idadevelho} anos!")



nomeDoVelho()
