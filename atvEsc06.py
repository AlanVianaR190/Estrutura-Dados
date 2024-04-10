def mediaDoVetor():
    import numpy

    #variavel com vetor de 3 valores vazio
    notas = numpy.empty(3,dtype="float64")

    #contador e acumulador
    acum = cont = 0

    #
    for c in range(3):
        notas[c] = float(input("Digite uma nota: "))
        acum += notas[c]
        cont +=1

    #variavel para calcular a media
    media = acum / cont

    #
    print(notas)

    #
    return f"{media:.2f}"


print(mediaDoVetor())
