from classes import Cronometro

meu_relogio = Cronometro()

meu_relogio.tic()
meu_relogio.tic()
meu_relogio.tic()
meu_relogio.tic()

meu_relogio.avançar(int(input('Digite quantos segundos o cronometro irá avançar: ')))

print(f'Tempo total: {meu_relogio.segundos}s')

meu_relogio.zerar()

print(f'Depois zerar o tempo agora é de: {meu_relogio.segundos}')