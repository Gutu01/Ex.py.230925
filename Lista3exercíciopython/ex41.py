total = float(input('Digite o total da conta:'))

pobres = int(total/3)
rico = total - pobres

print(f'Em uma conta de R${total:.2f} Gabriel e Maria pagaram R${pobres:.2f} e Willian pagará R${rico:.2f}')