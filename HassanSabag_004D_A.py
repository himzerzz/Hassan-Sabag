import datetime

# Entradas disponibles
platinum = [True] * 20
gold = [True] * 30
silver = [True] * 50

# Precios de las entradas
precios = {"platinum": 120000, "gold": 80000, "silver": 50000}

# Mostrar listado de asistentes
asistentes = []

# Definición de Funciones
def comprar_entradas():
    print("¿Cuántas entradas quiere comprar? (Máximo 3 entradas)")
    cant = int(input())
    if cant < 1 or cant > 3:
        print("Cantidad no válida, por favor ingrese una cantidad válida")
        return
    cat_asiento = ""
    while cat_asiento not in ["platinum", "gold", "silver"]:
        print("¿Qué categoría de asiento quiere? (platinum, gold, silver)")
        cat_asiento = input().lower()
    if cat_asiento == "platinum":
        disponibles = platinum
    elif cat_asiento == "gold":
        disponibles = gold
    else:
        disponibles = silver
    print("Asientos disponibles:")
    for i, disponible in enumerate(disponibles):
        if disponible:
            print(f"{i+1}: Disponible")
        else:
            print(f"{i+1}: Vendido")
    seleccionados = []
    while len(seleccionados) < cant:
        print(f"Seleccione asiento {len(seleccionados)+1}")
        seleccion = int(input())-1
        if seleccion < 0 or seleccion >= len(disponibles) or not disponibles[seleccion]:
            print("Asiento no disponible")
            continue
        seleccionados.append(seleccion)
        disponibles[seleccion] = False
    for i in range(cant):
        print(f"Ingrese RUN para la entrada {i+1}, sin guión ni dígito verificador")
        run = input()
        while not run.isnumeric() or len(run) != 8:
            print("RUN no válido, intentelo de nuevo")
            run = input()
        asistentes.append({"run": run, "categoria"})
