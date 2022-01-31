real = float(input('Quanto dinheiro voce tem na carteira?'))
dolar = real / 5.50
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))