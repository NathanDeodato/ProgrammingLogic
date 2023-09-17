# Média aritmética

print("-" * 100)
print("- Média aritmética -".center(100))
print("-" * 100)

nome = str(input("Nome do aluno: "))
serie = str(input("Série do aluno: "))

print("-" * 100)

print(f"- Este programa realizará o calculo da média aritmética do aluno: {nome}")

print("-" * 100)

nota_1 = float(input("1° nota: "))
nota_2 = float(input("2° nota: "))

print("-" * 100)

media = (nota_1 + nota_2) / 2

print(f"A média aritmética do aluno é: {media:.1f}")
