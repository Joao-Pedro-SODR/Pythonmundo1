import math
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(math.pow(catetoOposto, 2) + math.pow(catetoAdjacente, 2))

print(f"A hipotenusa vai medir: {hipotenusa:.2f}")