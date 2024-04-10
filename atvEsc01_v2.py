class CalculadoraDeMedia:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0  # Retorna 0 se não houver notas
        return f"{sum(self.notas) / len(self.notas):.1f}"

# Exemplo de uso
calculadora = CalculadoraDeMedia()

# Adicione as notas
n1 = float(input("Digite a nota: "))
calculadora.adicionar_nota(n1)

n2 = float(input("Digite a nota: "))
calculadora.adicionar_nota(n2)

n3 = float(input("Digite a nota: "))
calculadora.adicionar_nota(n3)

# Calcule a média
media = calculadora.calcular_media()
print(f'A média das notas é: {media}')



