n = input('Nome ')
s = float(input('Salário: R$ '))
a = s * 115 / 100
print('Salário de {} com aumento de 15% ficou R$ {:.2f}'.format( n , a))
td = a * 80/ 100
print('O desconto de 20% devido aos impostos totaliza o salário de {} em R$ {:.2f}'.format( n, td))

d = float(input('Compra de Reais  em doláres => R$ '))
print('Compra realizada por {}.\nSua carteira em doláres US${:.2f}'.format( n , d / 5.14 ))
cm = float(input('Mercado R$ '))
v = float(input('Vestuário R$ '))
f = float(input('Farmácia R$ '))
o = float(input('Outros R$ '))
tt = td - d - cm - f - o
print('O total de {} é R$ {:.2f}'.format( n , tt))
