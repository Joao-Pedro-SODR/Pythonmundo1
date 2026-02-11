"""
Tipo do valor
possui espaços 
é um número
é alfabético
é alfanúmerico
está em maiusculas 
está em minusculas
"""

valor = input("Digite algo: ")
print(f"O tipo primitivo dess valor é {type(valor)}")
print(f"Possui só espaços? {valor.isspace()}")
print(f"É numérico? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúsculas? {valor.islower()}")
print(f"Está Capitalizada? {valor.istitle()}")
