# Faça um programa que calcule a raiz quadrada de um numero e exiba o resultado.

numero = int(input("Entre com um numero para calcular a raiz quadrada: "))

raiz = numero ** 0.5
raiz = round(raiz,2)

print("Raiz quadrada de", numero, "é:", raiz)