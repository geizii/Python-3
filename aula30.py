"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
""" numero_digitado = int(input('Digite um número inteiro:'))

if numero_digitado.isdigit():
    print()
else: 
    print('Você não digitou um número inteiro')

if numero_digitado % 2 == 0:
    print('Este número é par')
else:
    print('Este número é impar')

if (numero_digitado) != False:
    print('O número não é inteiro') """


""" Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
""" 
hora = int(input("Qual é a hora ? "))

if hora >= 0 and hora < 11:
    print(f'Bom dia ! são {hora} horas')
elif hora >= 12 and hora < 18:
    print(f'Boa tarde ! são {hora} horas')
elif hora >= 18 and hora < 23: 
    print(f'Boa noite! são {hora} horas')
"""


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
""" 
username = input("Digite o seu nome: ")

contagem_username = len(username)

if contagem_username <= 4: 
    print('Seu nome é curto')
elif contagem_username >= 5 and contagem_username  < 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande') """