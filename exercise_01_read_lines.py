def read_lines(filename):

    # lista vacia donde se guardara todo

    lines = []

    # Abre el archivo en modo lectura ("r")
    with open(filename, "r") as file:

        # Recorre cada línea del archivo
        for line in file:

            # Elimina espacios al inicio/final y el salto de línea (\n)
            clean_line = line.strip()
            
            # Si la línea NO está vacía, se agrega a la lista
            if clean_line != "":
                lines.append(clean_line)

    return lines