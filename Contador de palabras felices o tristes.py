print("Bienvenido. Por favor, ingrese un texto de su preferencia:\n")
texto = input() #Texto ingresado

#Glosario de palabras a comparar 
felices = ["alegría", "feliz", "amor", "entusiasmo", "contento"]
tristes = ["triste", "llorar", "odio", "soledad", "miedo"]

palabras=texto.lower().split() #Dividir el texto en palabras haciendo un vector de palabras y poniendolas todas en minúsculas

#Contadores
numfeliz=0
numtriste=0
numnoco=0

#Recorre cada parametro dentro del vector "palabras" y lo almacena en un nuevo vector llamado "numero_palabras"
for palabra in palabras:
    #Compara la palabra almacenada con las palabras en el vector "felices"
    if palabra in felices:
        numfeliz+=1 #Si la palabra se encuentra en el vector "felices" suma
    elif palabra in tristes:
        numtriste+=1 #Si la palabra se encuentra en el vector "tristes" suma
    else:
        numnoco+=1 #Si la palabra no se encuentra en ninguno de los vectores

#Imprime el resultado de la comparación
print("El texto ingresado tiene", numfeliz, "palabras felices, ", numtriste, "palabras tristes y ",numnoco, "palabras que no coinciden")


        
        
