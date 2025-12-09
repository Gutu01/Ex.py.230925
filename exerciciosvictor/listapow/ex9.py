salario = float(input('Digite o seu salário: '))

conta_luz = 100
conta_agua = 100
boate_azul = 1200

salario_total = salario - conta_luz - conta_agua - boate_azul

print(f'Restou do seu salario apenas {salario_total:.2f}')
