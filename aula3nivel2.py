print("bem vindo a calculadora IMC")

nome = input("para começar digite o seu nome:")

altura = float( input("digite a sua altura: "))
peso = float(input("digite o seu peso: "))

imc = peso / ( altura * altura)

print(nome," seu IMC é", imc )