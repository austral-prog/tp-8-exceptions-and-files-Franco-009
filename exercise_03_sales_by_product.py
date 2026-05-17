def read_sales(filename):

    sales = {}

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        # Lee todo el contenido
        content = file.read()

        # Divide los registros usando ";"
        records = content.split(";")

        # Recorre cada registro
        for record in records:

            # Ignora registros vacÃ­os
            if record != "":

                # Divide producto y valor usando ":"
                product, value = record.split(":")

                # Convierte el valor a float
                value = float(value)

                if product in sales:
                    sales[product].append(value)
                else:
                    sales[product] = [value]

    return sales


def process_sales(data):

    for product in data:

        # Obtiene la lista de ventas
        values = data[product]

        # Calcula el total
        total = sum(values)

        # Calcula el promedio
        average = total / len(values)

        # Imprime el resultado con 2 decimales
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")