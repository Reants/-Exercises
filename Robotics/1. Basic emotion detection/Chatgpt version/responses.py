

def obtener_respuesta(emocion):
    """
    Devuelve una respuesta empática según la emoción detectada.
    """

    if emocion == "alegria":
        return "¡Me alegra mucho saber que te sientes así! 😄 Sigue disfrutando tu día."

    elif emocion == "tristeza":
        return "Siento que te sientas así 😔. Recuerda que no estás solo y todo puede mejorar."

    elif emocion == "enojo":
        return "Entiendo que estés molesto 😠. Respira profundo, a veces ayuda hablarlo."

    else:
        return "Gracias por compartir cómo te sientes. Estoy aquí para escucharte 🤖."
