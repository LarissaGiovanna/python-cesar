pesoProdutos = []
QuantProdutosVendidos = int(input("Digite a quantidade de produtos vendidos pela loja: "))

for i in range(QuantProdutosVendidos):
    peso = float(input("Digite o peso para o produto: "))
    pesoProdutos.append(peso)

pesoMedio = sum(pesoProdutos)/QuantProdutosVendidos
menorPeso = min(pesoProdutos)
maiorPeso = max(pesoProdutos)
arrecadacaoDia = sum(pesoProdutos)*4.35

print(f"Peso médio dos produtos: {pesoMedio:.2f}\nProduto com menor peso: {menorPeso}\nProduto com maior peso: {maiorPeso}\nArrecadação do dia: R$ {arrecadacaoDia}")