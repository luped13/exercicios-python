# if 2 is 3:
#     print('dois é igual a três')
# else:
#     print ('dois não é igual a três')

# print('Oi')


# Exercício 1 - Faça um programa que receba dois números e mostre o resultado das operações básicas.

n1 = int(input('Digite o número 10:'))
n2 = float(input('Digite o número 3:'))

soma = n1 + n2
print(soma)

subtração = n1 - n2
print (subtração)

multiplicação = n1*n2
print(multiplicação)

divisão = n1/n2
print(divisão)

CORREÇÃO
n1 = float(input('Digite o primeiro número:'))
soma = n1+n2
print("A soma dos números é "+str(soma)) ou
print(" A soma dos números é %f" % soma) ou
print(f"A soma dos números é {soma}")

# Exercício 2 - Faça um programa que receba quatro números e mostre a média entre os quatro.

n1 = int(input('Digite um número entre 0 e 10.'))
n2 = int(input('Digite um número entre 0 e 10.'))
n3 = int(input('Digite um número entre 0 e 10.'))
n4 = int(input('Digite um número entre 0 e 10.'))

media = (n1 + n2 + n3 + n4)/4
print(media)


# Exercício 3 - Faça um programa que receba uma temperatura em Celsius e retorne ela em Fahrenheit. A fórmula de conversão é: F = (C * 9/5) + 32

Celsius = int(input('Digite uma temperatura em Celsius e veja o resultado em Fahrenheit.'))

conversão = (Celsius * 9/5) + 32
print(conversão)


# Exercício 4 - Faça um programa que receba dois inputs, uma palavra/frase e uma letra. O programa deve retornar quantas vezes a letra apareceu na palavra/frase.

palavra = input('Digite uma palavra.')
letra = input('Digite uma letra.')


print(palavra.count(letra))


# Exercício 5 - Faça um programa que receba quantos números terá no cálculo da média e retorne a média deles. Exemplo: "Quantos números: 10" -> (n1+n2+n3+...+n10)/10.

qtd_numeros = int(input('Quantos números terá no cálculo da média?'))
numeros = 0
for in range (0,qtd_numeros)
    

media = numeros / qtd_numeros

print(media)








