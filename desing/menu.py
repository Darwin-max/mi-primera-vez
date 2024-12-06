from logic.formula import hi

def desing():
    print(f"Bienvenido al mejor programa del mundo ")
    print(f"     0. Atras")
    print(f"     1. Desde que muestre maquina salude ")
    opc = int(input(f"Eleji  una de las opciones deisponibles:  "))
    if (opc == 1):
        name = input("Ingrese su nombre ")
        reslta = hi (name)
        print(reslta)
    return opc