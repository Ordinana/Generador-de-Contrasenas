import random

print("GENERADOR DE CONTRASEÑAS")

facil = "abcdefghijklmnñopqrstuvwxyz"
media = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
dificil = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZª!@·$%&/()=?¿-0123456789"

while True:
    numeros = input("¿Cuántas contraseñas desea generar?: ")
    numeros = int(numeros)

    longitud = input("¿Cuántos carácteres para cada una?: ")
    longitud = int(longitud)

    grado = input("¿Qué nivel de seguridad quieres que tenga?\n"
                "Fácil: F\n"
                "Media: M\n"
                "Dificil: D\n"
                "")

    grado = grado.lower()

    print("\nAquí están tus contraseñas:\n")

    if grado == "f":
        for pwd in range(numeros):
            contraseñas = ""
            for c in range(longitud):
                contraseñas += random.choice(facil)
            print(contraseñas)
        

    if grado == "m":
        for pwd in range(numeros):
            contraseñas = ""
            for c in range(longitud):
                contraseñas += random.choice(media)
            print(contraseñas)
            

    if grado == "d":
        for pwd in range(numeros):
            contraseñas = ""
            for c in range(longitud):
                contraseñas += random.choice(dificil)
            print(contraseñas)
                
    print()
    otra = input("¿Desea nuevas contraseñas? (si/no): ")
    if otra == "si":
        pass
    else:
        break