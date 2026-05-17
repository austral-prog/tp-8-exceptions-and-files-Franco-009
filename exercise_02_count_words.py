def count_words(filename):

    # Diccionario donde se guardara la cantidad de words
    words_count = {}

    # Abre el archivo en modo lectura
    with open(filename, "r") as file:

        # Lee todo el contenido del archivo
        content = file.read()

        words = content.split()

        # Recorre cada palabra
        for word in words:

            word = word.lower()

            if word in words_count:
                words_count[word] += 1
            else:

                words_count[word] = 1

    return words_count