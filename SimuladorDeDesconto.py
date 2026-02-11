valorProduto  = float(input("Qual é o valor do produto? R$"))
valorDescontado  = valorProduto - (valorProduto * 5 / 100)

print(f"O produto que custava R${valorProduto}, com o desconto de 5% vai custar R${valorDescontado:.2f}")