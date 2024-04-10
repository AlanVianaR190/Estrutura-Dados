from datetime import datetime
from random import randint, choice
from time import sleep

class Atendimento:
    def __init__(self):
        self.senhas = []
        self.historico = []

    def horaData(self):
        agora = datetime.now()
        dh = agora.strftime("%d/%m/%y - %H:%M:%S")
        return dh

    def geradorCod(self):
        letra = tuple(("A","B","C","D","E"))
        numero = randint(10, 99)
        cod = choice(letra) + str(numero)

        while cod in self.senhas:
            cod = choice(letra) + str(numero)

        return cod

    def opcPers(self, lista):
        while True:
            print("O que deseja fazer: ")
            for pos, item in enumerate(lista):
                print(f"{pos+1} - {item}")
                sleep(0.5)
            print("")

            try:
                opcao = int(input("Digite uma das opções: "))
                if opcao >= 1 and opcao <= len(lista):
                    return lista[opcao-1]
                else:
                    print("ESTA OPÇÃO NÃO EXISTE!")
                    print("")
            except ValueError:
                print("OPÇÃO INVÁLIDA. Digite um número.")
                print("")

    def prefer(self):
        opcao = str(input("Atendimento preferencial [S]/[N]: ")).upper().strip()
        while opcao not in ("S", "N"):
            print("OPÇÃO INVALIDA!")
            opcao = str(input("Atendimento preferencial [S]/[N]: ")).upper().strip()

        if opcao == "S":
            return "SIM"
        else:
            return "NÃO"

    def geraSenha(self, listaMotiv):
        senha = {
            "SENHA": self.geradorCod(),
            "DATA & HORA": self.horaData(),
            "MOTIVO": self.opcPers(listaMotiv),
            "ATENDIMENTO PREFERENCIAL": self.prefer()
        }

        return senha

    def ticket(self, dicio, txt=""):
        for campo, info in dicio.items():
            print(f"{campo}: {info}", end=" | ")
        print(txt)
        print("")

    def filaSenha(self):
        if self.senhas:
            for pos, item in enumerate(self.senhas):
                print(f"{pos+1} - ", end="")
                self.ticket(item)
        else:
            print("NÃO CONTEM SENHAS NA LISTA!")
            print("")

    def chamaSenha(self):
        if self.senhas:
            chamada = self.verifPref()
            if chamada is None:
                chamada = self.senhas.pop(0)
            self.ticket(chamada, "O ATENDENTE O AGUARDA!")
        else:
            print("NÃO CONTEM SENHAS NA LISTA!")
            print("")

    def verifPref(self):
        for pos, item in enumerate(self.senhas):
            if item["ATENDIMENTO PREFERENCIAL"] == "SIM":
                return self.senhas.pop(pos)
        return None

    def finalSec(self):
        if self.senhas:
            print(f"NÃO E POSSIVEL SAIR. AINDA CONSTA {len(self.senhas)} SENHAS NA LISTA PARA SEREM CHAMADAS!\n")
            return " "
        else:
            resposta = self.verifSN()
            return resposta

    def verifSN(self):
        print("Responda apenas sim[s] / não[n]...")
        resp = str(input("Deseja encerrar o programa? ")).upper().strip()[0]
        print()

        while resp not in("S", "N"):
            print("Responda apenas sim[s] / não[n]...")
            resp = str(input("Deseja encerrar o programa? ")).upper().strip()[0]
            print()

        return resp

    def salvarHist(self):
        agora = datetime.now()
        dh = agora.strftime("%d/%m/%y-%H:%M:%S")

        with open("C:/Users/Maria/Desktop/historico_" + dh.replace("/", "_").replace(":", "_") + ".txt", "w") as arquivo:
            for item in self.historico:
                arquivo.write(str(item) + "\n")

    def run(self):
        while True:
            tupla = tuple(("GERAR SENHA", "MOSTRAR FILA DE SENHAS", "CHAMAR PROXIMA SENHA", "SAIR"))
            opc = self.opcPers(tupla)

            if opc == "GERAR SENHA":
                tupla1 = tuple(("ABERTURA DE CONTA", "DEPOSITO E SAQUE", "PAGAMENTOS", "FINANCIAMENTOS", "INVESTIMENTOS"))
                senha = self.geraSenha(tupla1)
                self.senhas.append(senha.copy())
                self.ticket(senha, "AGUARDE POR FAVOR!")
                self.historico.append(senha)

            elif opc == "MOSTRAR FILA DE SENHAS":
                self.filaSenha()

            elif opc == "CHAMAR PROXIMA SENHA":
                self.chamaSenha()

            elif opc == "SAIR":
                sair = self.finalSec()
                if sair == "S":
                    break

        print("PROGRAMA ENCERRADO")
        self.salvarHist()


# Instanciar a classe e executar o programa
atendimento = Atendimento()
atendimento.run()
