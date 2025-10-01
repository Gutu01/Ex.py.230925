pequeno = int(input('Digite a quantidade de camisetas pequenas: '))
media = int(input('Digite a quantidade de camisetas média: '))
grande = int(input('Digite a quantidade de camisetas grandes: '))

total = pequeno*10 + media*12 + grande*15

print(f'Fica: R${total:.2f}')