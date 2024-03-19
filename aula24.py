""" 
Formatação básica de strings em Python

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - centro
Sinal - + ou -
Ex.: 0 > 100,.1f
Conversion flags -  !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')