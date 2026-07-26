print("""
<<< CONTADOR DE IMPARES O PARES >>>

-- Dada una lista de números determinar cuantos son impares o pares

""")

def contar_pares(nums):
    pares = 0
    impares = 0
    for i in nums:
        if i % 2 == 0:
            pares+=1
        else:
            impares+=1
    return pares,impares

l_numeros = []
for i in range(10):
    num_i = int(input("> Número {}: ".format(i+1)))
    l_numeros.append(num_i)

par, impar = contar_pares(l_numeros)
print(f"""
- PARES:{par}
- IMPARES: {impar}
""")