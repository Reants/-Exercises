# 🤖 Ejercicio 2: Robot social con estado emocional persistente

## 📌 Título del ejercicio
Simulación de un robot social con estado emocional

## 🎯 Objetivo
Aprender a:
- Manejar **estados internos** en un robot simulado
- Mantener una **emoción activa** en el tiempo
- Cambiar el comportamiento del robot según su emoción actual
- Reforzar lógica condicional y funciones en Python

## 🧰 Tecnologías usadas
- Python 3
- Consola / terminal

## 📚 Conceptos que se practican
- Variables de estado
- Condicionales (`if / elif / else`)
- Funciones
- Entrada del usuario (`input`)
- Lógica de comportamiento
- Simulación de emociones simples

## 📝 Instrucciones paso a paso

1. Crea un archivo llamado `robot_emocional.py`
2. Define una variable llamada `emocion_actual`
   - Su valor inicial debe ser `"neutral"`
3. Crea una función llamada `detectar_emocion(mensaje)`
   - Recibe un texto
   - Devuelve una emoción según palabras clave:
     - `"feliz"` si el mensaje contiene palabras positivas
     - `"triste"` si contiene palabras negativas
     - `"neutral"` si no detecta nada
4. Crea una función llamada `responder_robot()`
   - Usa la variable `emocion_actual`
   - Imprime una respuesta distinta según la emoción:
     - feliz → mensaje alegre
     - triste → mensaje empático
     - neutral → mensaje neutro
5. En un bucle:
   - Pide al usuario que escriba un mensaje
   - Actualiza `emocion_actual` usando `detectar_emocion`
   - Llama a `responder_robot`
6. El programa solo termina si el usuario escribe `"salir"`

## 📦 Qué debo entregar
- Archivo `robot_emocional.py`
- El código debe ejecutarse sin errores
- El robot debe **recordar su emoción** entre mensajes

## ✅ Criterios de evaluación (nivel junior)
- El programa corre correctamente
- Uso correcto de condicionales
- La emoción se guarda y se reutiliza
- El código es legible y ordenado
- Uso correcto de funciones

## 🚀 Reto opcional (muy simple)
- Agrega una emoción extra (`"enojado"` o `"sorprendido"`)
- Cambia la respuesta del robot según esa emoción
