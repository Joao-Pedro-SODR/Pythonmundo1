diasAlugados = int(input("Quantos dias alugados? "))
kmRodados = int(input("Quantos km rodados? "))

total = diasAlugados * 60 + kmRodados * 0.15

print(f"O total a pagar é de R${total:.2f}")