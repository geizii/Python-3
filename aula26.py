nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
nome_invertido = nome[::-1]
n = len(nome)


if nome and idade: 
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if '' in nome:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaço')
    
    print(f'Seu nome tem {n} letras')
    print(f'A primeira letra do seu nome {nome[0]}')
    print(f'A última letra do seu nome {nome[-1]}')
else: 
    print("Desculpe, você deixou campos vazios")


