lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
lista_sin_duplicados = list(dict.fromkeys(lista))
lista_sin_duplicados = sorted(set(lista), reverse=True)
lista_pares = [num for num in lista if num % 2 == 0]

print(lista_sin_duplicados)
print(lista_pares)
suma_pares = sum(lista_pares)
print(suma_pares)
lista_pares.insert(0, suma_pares)
print(lista_pares)
