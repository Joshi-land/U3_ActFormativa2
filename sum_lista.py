print("""
<<<< SUMA DE NÚMEROS (LISTA) >>>>

- Se ingresaran una serie de números que se almacenaran en una lista para posteriormente sumarlos

""")

def suma_lista(lista_num):
    suma = 0
    for num in lista_num:
        suma += num
    return suma

lista_num_in = []
for i in range (5):
    valor = int(input(f"- Ingrese número {i+1}: "))
    lista_num_in.append(valor)

total = suma_lista(lista_num_in)
total_functsum = sum(lista_num_in)

print("\n- Suma con bucle: ", total)
print("\n- Suma con función sum(): ", total_functsum)