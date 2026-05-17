def write_inventory(filename, inventory):

    # Abre el archivo en modo escritura
    # "w" sobreescribe el archivo si ya existe
    with open(filename, "w") as file:

        # Obtiene los items ordenados alfabéticamente
        items = sorted(inventory)

        # Recorre cada item
        for item in items:
            # Obtiene la cantidad
            quantity = inventory[item]
            # Escribe la línea con formato item:cantidad
            file.write(f"{item}:{quantity}\n")