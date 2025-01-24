print("Bienvenido a su calculadora virtual\nPor favor, seleccione una de las opciones")
seleccion=input("\n 1.Suma\n 2.Resta\n 3.Multiplicación\n 4.División\n")

match seleccion:
    case "1":
        print("\nUsted ha seleccionado suma")
        x=int(input("\nIngrese su primer valor:"))
        y=int(input("\nIngrese su segundo valor:"))
        resultado=x+y
        print(f"su resultado para {x} + {y} es={resultado}\n")        
    case "2":
        print("\nUsted ha seleccionado resta")
        x=int(input("\nIngrese su primer valor:"))
        y=int(input("\nIngrese su segundo valor:"))
        resultado=x-y
        print(f"su resultado para {x} - {y} es={resultado}")  
    case "3":
        print("\nUsted ha seleccionado multiplicación")
        x=int(input("\nIngrese su primer valor:"))
        y=int(input("\nIngrese su segundo valor:"))
        resultado=x*y
        print(f"su resultado para {x} * {y} es={resultado}")
    case "4":
        print("\nUsted ha seleccionado división")
        x=int(input("\nIngrese su primer valor:"))
        y=int(input("\nIngrese su segundo valor:"))
        if y!=0:
            resultado=x/y
            print(f"su resultado para {x} / {y} es={resultado}")
        else:
            print("No se puede dividir entre cero")
    case _:
        print("Opción no válida")
        print("Gracias por utilizar nuestra calculadora virtual")
    
