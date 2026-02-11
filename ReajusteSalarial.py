salario = float(input("Qual é o salario do Funcionário? "))

novoSalario = salario + (salario * 15/100)
print(f"O Funcionário que ganhava R${salario}, com 15% de aumento, passa a receber {novoSalario:.2f}")