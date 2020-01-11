# allpython
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

soma = 0
maior = 0
menor = 0
cont = 0

n = int(input('Quantos números quer digitar? '))

while (cont < n):
    num = int(input('Informe um número: '))

    while (num < 0) or (num > 1000):
        print('número inválido')
        num = int(input('Informe um número: '))

    cont += 1
    soma += num
    
    if (num > maior):
        maior = num
    if (menor == 0) or (num < menor):
        menor = num

print(soma,maior,menor)
