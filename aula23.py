""" 
Interpolação básica de strings em Python

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Geizi'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d e %04x' % (15, 15))