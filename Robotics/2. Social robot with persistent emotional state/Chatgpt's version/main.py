# -----------------------------
# Robot Social con Estado Emocional Persistente
# -----------------------------

def detectar_emocion(texto):
    """
    Detecta la emoción del texto ingresado por el usuario.
    Retorna: 'feliz', 'triste', 'enojado' o 'neutro'
    """
    palabras_felicidad = ["feliz", "contento", "alegre", "bien", "genial"]
    palabras_tristeza = ["triste", "mal", "deprimido", "cansado", "solo"]
    palabras_enojo = ["enojado", "molesto", "furioso", "irritado", "odio"]

    palabras = texto.split()

    for palabra in palabras:
        if palabra in palabras_felicidad:
            return "feliz"
        elif palabra in palabras_tristeza:
            return "triste"
        elif palabra in palabras_enojo:
            return "enojado"

    return "neutro"


def responder_emocion(emocion):
    """
    Genera una respuesta empática según la emoción actual del robot.
    """
    if emocion == "feliz":
        return "😊 Me alegra saber que te sientes bien. ¡Eso es genial!"
    elif emocion == "triste":
        return "😢 Siento que estés pasando por un momento difícil. Estoy aquí contigo."
    elif emocion == "enojado":
        return "😠 Parece que algo te ha molestado. Respiremos juntos un momento."
    else:
        return "😐 Estoy aquí para escucharte. Cuéntame más."


def main():
    print("🤖 Hola, soy tu robot social.")
    print("Cuéntame cómo te sientes. Escribe 'salir' para terminar.\n")

    estado_emocional = "neutro"

    while True:
        texto_usuario = input("Tú: ").lower()

        if texto_usuario == "salir":
            print("🤖 Gracias por hablar conmigo. ¡Hasta pronto!")
            break

        emocion_detectada = detectar_emocion(texto_usuario)

        # Actualizar estado solo si se detecta una emoción
        if emocion_detectada != "neutro":
            estado_emocional = emocion_detectada

        respuesta = responder_emocion(estado_emocional)
        print("🤖", respuesta)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
