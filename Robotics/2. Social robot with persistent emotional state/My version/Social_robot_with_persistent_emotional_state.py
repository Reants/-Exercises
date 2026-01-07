happy = ["feliz","emocionado","contento"]
sad = ["triste","apagado", "desanimado"]
angry = ["enojado", "molesto", "irritado"]

def emotion_detection(text):
    words = text.split()

    for word in words:
        if word in happy:
            return "happy"
        elif word in sad:
            return "sad"
        elif word in angry:
            return "angry"
        
    return "neutro"
    

def response(text):
    if text == "happy": print("\nEy que cool, hoy estamos felices. Me alegro por ti\n")    
    elif text == "sad": print("\nLamento leerte así de desanimado.\n")
    elif text == "angry": print("\nOh changos, estás molesto. Creo que mejor te dejo tranquilo\n")
    else: print("No estoy seguro de cómo te sientes, pero estoy aquí.")

def main():
    actual_emotion = "neutro"
    while True:
        answer = input("¿Cuentame como te sientes?\n").lower()
        new_emotion = emotion_detection(answer)
        if new_emotion != "neutro": actual_emotion = new_emotion
        response(actual_emotion)
        if answer == "salir":
            print("Hasta luego, nos vemos pronto")
            break
    
if __name__ == "__main__": 
    try:
        main()
    except ValueError:
        print("Entrada inválida. Por favor, introduce solo números enteros.")
