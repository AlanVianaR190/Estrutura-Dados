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

#principal
semana = tuple(("Domingo","Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado"))

#
while True:

    #
    num = int(input("Digite um numero de 1 ha 7 para saber o dia da semana: "))
    while num < 1 or num > 7:
        print("Este numero não corresponde a nenhum dia da semana!")
        num = int(input("Digite um numero de 1 ha 7 para saber o dia da semana: "))
    print(semana[num - 1])
    print()

    #
    opc = verifSN("Deseja continuar?")

    #
    if opc in("s"):
        continue
    else:
        break

print("Programa Encerrado")
