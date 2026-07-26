print("""
<<<< ENCONTRAR MÁXIMO Y MÍNIMO >>>>

- Dados 8 números encontrar el valor máximo y el mínimo
""")

def find_max(lista_num):
    if len(lista_num) == 0:
        return None
    maximo = lista_num[0]
    for num in lista_num [1:]:
        if num > maximo:
            maximo = num
    return maximo

def find_min(lista_num):
    if len(lista_num) == 0:
        return None
    minimo = lista_num[0]
    for num in lista_num[1:]:
        if num < minimo:
            minimo = num
    return minimo


lista_num_in = []

for i in range(8):
    valor = int(input(f"> Número {i+1}: "))
    lista_num_in.append(valor)

maximo_bucle = find_max(lista_num_in)
minimo_manual = find_min(lista_num_in)

print("\n> Máximo: ", maximo_bucle)
print("\n> Mínimo: ", minimo_manual)


