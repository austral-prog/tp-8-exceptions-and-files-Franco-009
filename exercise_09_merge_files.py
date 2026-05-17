def merge_files(file1, file2, output):

    # Abre y lee el primer archivo
    with open(file1, "r") as first_file:
        content1 = first_file.read()

    # Abre y lee el segundo archivo
    with open(file2, "r") as second_file:
        content2 = second_file.read()

    # Recién después de leer ambos archivos,
    # se crea/escribe el archivo de salida
    with open(output, "w") as out_file:

        # Escribe primero el contenido del primer archivo
        out_file.write(content1)

        # Luego escribe el contenido del segundo archivo
        out_file.write(content2)