# Essa função imprime um texto no terminal
# print("Hello World!")

'''
 Tipos de dados:

 str - string (texto)
 int - inteiro (número)
 float - ponto flutuante (número)
'''

msg = "python"      # É um dado tipo str
a = "3"             # É um dado tipo str
salario = 10000.50  # É um dado tipo float

# Função type: retorna o tipo do dado
print(f"Tipo de msg:{type(msg)}")               # Esperamos 'str'
print(f"Tipo de a:{type(a)}")                   # Esperamos 'str'
print(f"Tipo de salario:{type(salario)}")       # Esperamos 'float'

# Convertendo 'a' para float
a = float(a)
print(f"Tipo de a:{type(a)}")          # Esperamos 'float'