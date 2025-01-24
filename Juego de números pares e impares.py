while True:
    print("Bienvenido, ingrese por favor un número para empezar\n")
    num= input() #entra un dato
    
    #Valida si es un numero
    if num.isdigit(): 
        num= int(num)
        print("\nEl número ingresado es:", num)
        res=num % 2 #Módulo de num entre 2
        if res==0:
            print("El número ingresado es par")
        else:
            print("El número ingresado es impar")
        break #Cerrar el ciclo
    else:
        print("El número ingresado no es un número entero, por favor ingrese un número")
    
