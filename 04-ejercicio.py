while True:
    # Solicitar los dos números al usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    while True:

        # Mostrar menú
        print("\nMENU:")
        print("1. Sumar los dos números")
        print("2. Restar los dos números (primero - segundo)")
        print("3. Multiplicar los dos números")
        print("4. Salir del programa")

        # Solicitar opción
        opcion = input("Elige una opción (1-4): ")

        # Procesar opción
        if opcion == '1':
            print(f"\nResultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':
            print(f"\nResultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':
            print(f"\nResultado: {num1} × {num2} = {num1 * num2}")
        elif opcion == '4':
            print("\n nos vemos")
            break
        else:
            print("\n Opción no válida. Por favor elige del 1 al 4")
            continue
