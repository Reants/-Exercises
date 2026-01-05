# emotions.py

def detectar_emocion(texto):
    """
    Analiza el texto del usuario y devuelve la emoción detectada.
    """

    alegria = ["feliz", "emocionado", "contento"]
    tristeza = ["triste", "apagado", "desanimado"]
    enojo = ["enojado", "molesto", "irritado"]

    for palabra in alegria:
        if palabra in texto:
            return "alegria"

    for palabra in tristeza:
        if palabra in texto:
            return "tristeza"

    for palabra in enojo:
        if palabra in texto:
            return "enojo"

    return "neutral"
