def safe_average(filename):

    # Lista donde se guardarán los números válidos
    numbers = []

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        for line in file:
            # Elimina espacios y saltos de línea
            clean_line = line.strip()

            # Ignora líneas vacías
            if clean_line != "":
                try:
                    # Intenta convertir la línea a float
                    number = float(clean_line)

                    # Guarda el número válido
                    numbers.append(number)

                # Si no se puede convertir, se ignora
                except ValueError:
                    pass

    if len(numbers) == 0:
        # Lanza un error si no hay numeros validos
        raise ValueError("no valid numbers")

    # Calcula el promedio
    average = sum(numbers) / len(numbers)

    # Retorna el promedio
    return average