produtos = ['arroz','feijao','suamae'] 
quantidade = [10, 30, 1] 

pesquisa_pura = input('Digite o produtor a ser procurado: ') 
pesquisa = pesquisa_pura.lower() 
if pesquisa in produtos: 
    indice_pesquisa = produtos.index(pesquisa) 
    print(indice_pesquisa) 
    print(f'Quantidade no estoque: {quantidade[indice_pesquisa]}')