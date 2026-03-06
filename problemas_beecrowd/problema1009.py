#Receba os dados:
nome = input()               #str
salario = float(input())     #float
total_vendas = float(input())#float

# Calcule o total a receber...
total_receber = (salario + \
    (15/100)*total_vendas)

# Imprima na tela...
print(f"TOTAL = R$ {total_receber:.2f}")