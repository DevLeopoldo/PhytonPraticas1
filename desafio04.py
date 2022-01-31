Portugues = float(input('Digite a Nota de Portugues: '))
Matematica = float(input('Digite a nota de Matematica: '))
Quimica = float(input('Digite a nota de Quimica: '))

s = Portugues + Matematica + Quimica
m = s / 3
print('Essa é sua nota de Portugues: {}'.format(Portugues))
print('Essa é sua nota de Matematica: {}'.format(Matematica))
print('Essa é sua nota de Quimica: {}'.format(Quimica))
print('Parabens voce foi aprovado, essa é sua media geral: {}'.format(m))