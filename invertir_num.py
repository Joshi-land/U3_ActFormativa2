print("""
<<<< INVERTIR ORDEN LISTA >>>>

- Guardar una lista y posteriormente invertir el orden de esta

""")

def invertir(lista_num):
    invertida = []
    for i in range (len(lista_num),-1 , -1):
        invertida.append(i)
    return invertida
    
lista_num_in = []

for i in range (6):
    valor = int(input(f"> Número {i+1}: "))
    lista_num_in.append(valor)

print("\n> Lista original: ",lista_num_in)

invertida = invertir(lista_num_in)
print("\n> Invertida: ", invertida)