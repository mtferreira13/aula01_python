#Desafio aula1 - Cálculo de Bônus com Entrada do Usuário
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o seu bônus: "))

salario_bonus = 1000 + salario * bonus


print(f"Olá sr(a) {nome}, o seu bônus foi de: {salario}")