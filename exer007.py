larg = float(input('largura da parede: '))
alt = float(input('ALtura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce precisa de {}l de tinta.'.format(tinta))