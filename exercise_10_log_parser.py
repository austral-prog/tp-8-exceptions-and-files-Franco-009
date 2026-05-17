def parse_log(filename):

    # Diccionario donde se guardarán:
    # nivel -> lista de mensajes
    logs = {}

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        # Recorre cada línea
        for line in file:

            # Elimina espacios y saltos de línea
            clean_line = line.strip()

            # Ignora líneas vacías
            if clean_line != "":

                # Si la línea no tiene :
                if ":" not in clean_line:

                    # Lanza un error
                    raise ValueError("invalid log line")

                # Divide usando SOLO el primer :
                level, message = clean_line.split(":", 1)

                # Elimina espacios sobrantes
                level = level.strip()
                message = message.strip()

                # Si el nivel ya existe
                if level in logs:

                    logs[level].append(message)

                else:

                    # Crea la lista con el primer mensaje
                    logs[level] = [message]

    return logs