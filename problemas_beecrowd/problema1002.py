raio = float(input())
pi = 3.14159

area = pi*(raio**2)
print(f"A={area:.4f}")


def isEven(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return False
    elif number == 4:
        return True
    elif number == 5:
        return False
    elif number == 6:
        return True
    

    # Sintaxe: <valor_se_verdadeiro> if <condicao> else <valor_se_falso>
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)  # Saída: Maior de idade

