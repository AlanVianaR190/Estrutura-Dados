def maiorDoVetor():
    import numpy

    #variavel para prencher o valor do maior
    maior = 0

    #variavel para prencher o vetor com cinco valores
    numeros = numpy.random.randint(10, size=5, dtype="int32")

    #laço <for> para fazer a varredura
    for numero in numeros:

        #condição para pegar o maior valor
        if numero > maior:
            maior = numero

    #
    print(numeros)

    #
    print(maior)



maiorDoVetor()
