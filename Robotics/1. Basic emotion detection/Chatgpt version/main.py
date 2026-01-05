# main.py

from emotions import detectar_emocion
from responses import obtener_respuesta

def main():
    print("🤖 Hola, soy tu robot social.")
    print("Puedes contarme cómo te sientes hoy.\n")

    while True:
        texto_usuario = input("🧑 Tú: ").lower()

        emocion = detectar_emocion(texto_usuario)
        respuesta = obtener_respuesta(emocion)

        print(f"🤖 Robot: {respuesta}")

        continuar = input("\n¿Quieres seguir hablando? (si/no): ").lower()
        if continuar != "si":
            print("\n🤖 Robot: Gracias por hablar conmigo. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
