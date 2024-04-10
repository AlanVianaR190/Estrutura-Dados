#função
def separaPares(lista):
    '''
    Este metodo separa os pares dos impares pondo os em uma lista separadas
    :param lista: uma lista com numeros inteiros
    :return: sem retorno
    '''
    numeros = lista

    #
    par = list()
    impar = list()

    #
    for numero in numeros:

        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

    #
    print("Pares: ")
    print(par, end="  ")
    print("\n")
    print("Impares: ")
    print(impar, end="  ")


#programa
valores = list()

#
while True:
    num = int(input("Digite um numero; ou 999 p/ encerrar: "))
    if num == 999:
        break
    else:
        valores.append(num)

print("\n")
print("Lista de numeros:")
print(valores)
print("\n")

#chamar função
separaPares(valores)
