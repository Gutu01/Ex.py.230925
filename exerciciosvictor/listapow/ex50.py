frases = []

total_caratere = 0
quantidades_suamae = 0
i = 0
maior_frase = ''


while True:
    try:
        frases.append(input('Digite uma frase ou 0 para sair: '))

        if frases[-1] == '0':
            frases.remove('0')
            break
        else:
            total_caratere += len(frases[-1])
            if 'SUA MÃE' in frases[-1].upper():
                quantidades_suamae += 1

            if i == 0:
                maior_frase = frases[-1]
            else:
                if len(frases[-1]) > len(maior_frase):
                    maior_frase = frases[-1]

            i += 1
            continue

    except ValueError:
        print('Valor inválido!')

print(f'O total de frases digitadas foram de {frases}')
print(f'O total de caracteres registradas foram de {total_caratere}')
print(f'A maior frase é {maior_frase}')
print(f'a quantidade de vezes que sua mãe aparece é de {quantidades_suamae}')