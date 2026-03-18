from classes import Televisao

televisaotop = Televisao()

televisaotop.aumentar_volume()
televisaotop.aumentar_volume()
televisaotop.aumentar_volume()
televisaotop.aumentar_volume()

televisaotop.diminuir_volume()
televisaotop.diminuir_volume()

televisaotop.trocar_canal(float(input('Digite o número do canal desejado: ')))

print(f'Canal atual: {televisaotop.canal}')
print(f'Volume atual: {televisaotop.volume}')