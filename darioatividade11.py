# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input("qual a distancia que você irá percorrer na sua viagem em km? "))
if km <= 200:
     print("o preço da sua viagem é de: R$" , km * 0.50)
else:
     print("o preço da sua viagem é de: R$" , km * 0.45)