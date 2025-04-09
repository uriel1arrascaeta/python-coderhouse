
# basededatos
base_de_datos = {
    "heber": "clave123",
}

# verifico datos


def login(usuario, contraseña):
    if usuario in base_de_datos and base_de_datos[usuario] == contraseña:
        print("Bienvenido")
    else:
        print("Usuario o contraseña incorrectos")


def registrar(usuario, contrasena):
    """Registro un nuevo usuario si no existe."""
    if usuario in base_de_datos:
        print(" El usuario ya existe.")
        return False
    else:
        base_de_datos[usuario] = contrasena
        print(f" Usuario '{usuario}' registrado con éxito.")
        return True


def menu():
    """Muestro el menu principal."""
    print(" Menú de Login")
    print("1Iniciar sesión")
    print("2 Registrarse")
    print("3 Salir")
    opcion = input("Elegí una opción (1/2/3): ")

    if opcion == "1":
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        login(usuario, contrasena)
    elif opcion == "2":
        usuario = input("Nuevo usuario: ")
        contrasena = input("Elegí una contraseña: ")
        registrar(usuario, contrasena)
    elif opcion == "3":
        print("nos vemos")
        return False
    else:
        print(" Opción no válida.")
    return True

# Ejecuto el programa
# Bucle


def ejecutar_programa():
    continuar = True
    while continuar:
        continuar = menu()


ejecutar_programa()
