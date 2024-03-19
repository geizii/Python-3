""" 
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao: 
    nome = input('Qual seu nome ?')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou') 