def csv_to_dict(filename):

    people = []

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        # Lee todas las líneas
        lines = file.readlines()

        # Si el archivo está vacío o solo tiene header (primero)
        if len(lines) <= 1:
            return []

        # Obtiene el header y elimina espacios/saltos
        headers = lines[0].strip().split(",")

        # Recorre las líneas de datos
        for line in lines[1:]:

            # Elimina espacios y saltos de línea
            clean_line = line.strip()

            # Divide los valores usando ,
            values = clean_line.split(",")

            person = {}

            # Recorre índices del header
            for i in range(len(headers)):

                # Obtiene clave y valor con strip
                clave = headers[i].strip()
                valor = values[i].strip()

                # Convierte age a int
                if clave == "age":
                    valor = int(valor)

                # Guarda en el diccionario
                person[clave] = valor

            people.append(person)

    return people