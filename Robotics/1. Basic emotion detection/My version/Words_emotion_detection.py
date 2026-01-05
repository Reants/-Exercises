Alegria = ["feliz","emocionado","contento"]
Tristeza = ["triste","apagado", "desanimado"]
Enojo = ["enojado", "molesto", "irritado"]

def happy (input):
    words = input.split()
    for word in words:
        if word in Alegria:
            return 1
    return 0
            
def sad (input):
    words = input.split()
    for word in words:
        if word in Tristeza:
            return 1
    return 0

def angry (input):
    words = input.split()
    for word in words:
        if word in Enojo:
            return 1
    return 0

def main():
    while(True):
        response=input("Hola, mucho gusto. Yo soy tu asistente robot emocional. ¿Cómo te sientes el día de hoy?\n")
        H = happy(response)
        S = sad(response)
        A = angry(response)
        if H == 1 and S == 0 and A == 0: print("\nHe detectado que estás feliz. Me da mucho gusto saber esto y espero puedas continuar el día así")

        elif H == 0 and S == 1 and A == 0: print("\nHe detectado que estás triste y quiero decirte que estoy aqui para apoyarte. Tal vez no pueda abrazarte, pero puedo acompañarte y hablar contigo siempre que lo necesites")

        elif H == 0 and S == 0 and A == 1: print("\nHe detectado que estás enojado. Quisieras contarme por que estás así o prefieres tomarte un respiro?")

        else: 
            print("No he logrado detectar una de las tres emociones que tengo asignadas.\n")
        
        retry = input("Quisieras volver a iniciar? (Y/N)")
        if retry == "Y" or retry == "y":
            continue
        elif retry == "N" or retry == "n":
            print("Gracias por hablar conmigo. Nos vemos pronto")
            break
        else:
            print("No has seleccionado una de las opciones indicadas. Por eso terminaré con mis funciones, que tengas un excelente día.")
            break

if __name__ == "__main__": 
    try:
        main()
    except ValueError:
        print("Entrada inválida. Por favor, introduce solo números enteros.")
