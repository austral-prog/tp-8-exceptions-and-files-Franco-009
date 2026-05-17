def find_longest_word(filename):

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        # Lee todo el contenido
        content = file.read()
        # Divide el texto en palabras
        words = content.split()

    if len(words) == 0:
        # Lanza un error si no hay words !!!
        raise ValueError("file has no words")

    # La palabra más larga empieza siendo la primera
    longest_word = words[0]
    # Recorre cada palabra para comprobar
    for word in words:
        # Si la palabra actual es más larga
        if len(word) > len(longest_word):
            # Se convierte en la nueva más larga
            longest_word = word

    return longest_word