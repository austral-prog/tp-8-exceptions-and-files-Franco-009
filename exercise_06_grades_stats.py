def grades_stats(filename):

    # Diccionario donde se guardarán
    # estudiante (promedio, maximo, minimo)
    stats = {}

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        # Recorre cada línea
        for line in file:
            # Elimina espacios y saltos de línea
            clean_line = line.strip()
            # Ignora líneas vacías
            if clean_line != "":
                # Divide nombre y notas usando :
                student, grades = clean_line.split(":")
                # Divide las notas usando ,
                grades_list = grades.split(",")
                # Lista donde se guardarán las notas como float
                numbers = []
                # Recorre cada nota
                for grade in grades_list:
                    # Convierte la nota a float
                    numbers.append(float(grade))

                # Calcula promedio
                average = sum(numbers) / len(numbers)
                # Calcula máximo
                maximum = max(numbers)
                # Calcula mínimo
                minimum = min(numbers)
                # Guarda la tupla en el diccionario
                stats[student] = (average, maximum, minimum)

    return stats