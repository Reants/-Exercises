# 🤖 Robot Social con Estado Emocional Persistente (Python)

## 1. Descripción del ejercicio
En este proyecto se desarrolla un **simulador de robot social** que interactúa con una persona mediante texto y es capaz de **mantener un estado emocional persistente** a lo largo de la conversación.

El robot:
- Recibe frases escritas por el usuario
- Detecta emociones básicas mediante palabras clave
- Mantiene la última emoción detectada como estado interno
- Responde de forma empática según su estado emocional actual

Este ejercicio **no utiliza inteligencia artificial avanzada**, sino **lógica básica en Python**, simulando cómo un robot social puede empezar a interpretar emociones humanas y recordarlas.

---

## 2. Objetivo de aprendizaje
Al finalizar este ejercicio serás capaz de:

- Aplicar **lógica condicional** para detección emocional
- Procesar texto ingresado por el usuario
- Mantener un **estado interno persistente**
- Separar responsabilidades mediante funciones
- Simular una interacción básica de **Human–Robot Interaction (HRI)**
- Escribir código claro, legible y estructurado (nivel Junior)

---

## 3. Tecnologías usadas
- Python 3.x
- Consola / Terminal

---

## 4. Requisitos previos
- Conocimientos básicos de Python:
  - Variables
  - Listas
  - Condicionales (`if / elif / else`)
  - Funciones
  - Bucles (`while`)

> No se utilizan librerías externas.

---

## 5. Instrucciones paso a paso

### 🧩 Etapa 1: Preparar el entorno
1. Crear una carpeta para el proyecto
2. Crear un archivo principal en Python (`main.py`)
3. Ejecutar el archivo desde la terminal con Python 3

---

### 🧠 Etapa 2: Entrada del usuario
- Solicitar al usuario que escriba cómo se siente
- Convertir el texto a minúsculas para facilitar la comparación
- Mantener el programa en ejecución hasta que el usuario escriba `"salir"`

---

### 😊 Etapa 3: Detección emocional
- Definir listas de palabras clave para cada emoción:
  - Felicidad
  - Tristeza
  - Enojo
- Dividir el texto del usuario en palabras
- Comparar cada palabra con las listas emocionales
- Retornar la emoción detectada o `"neutro"` si no se detecta ninguna

---

### 🤖 Etapa 4: Estado emocional persistente
- Inicializar el estado emocional del robot como `"neutro"`
- Actualizar el estado **solo cuando se detecte una emoción**
- Mantener la emoción anterior si no se detecta una nueva

---

### 🔁 Etapa 5: Respuesta del robot
- Generar una respuesta empática según el estado emocional actual
- El robot responde incluso si la emoción fue detectada en una interacción anterior

---

## 6. Estructura del proyecto

```text
social-robot-persistent-emotion/
│
├── main.py
└── README.md
``` 
---

## 7. Revisión del código (errores y mejoras)

| Área              | Observación                             | Explicación                               | Mejora sugerida                      |
| ----------------- | --------------------------------------- | ----------------------------------------- | ------------------------------------ |
| Manejo de errores | Uso de `try/except ValueError`          | No se realizan conversiones numéricas     | Eliminar el bloque `try/except`      |
| Flujo de salida   | El robot responde al escribir `"salir"` | La condición de salida se evalúa al final | Validar `"salir"` antes de responder |
| Estado neutro     | No hay respuesta para estado `"neutro"` | El usuario no recibe feedback inicial     | Agregar respuesta neutral            |
| Normalización     | No se manejan acentos                   | Palabras como `"felíz"` no se detectan    | Ampliar listas o normalizar texto    |

---
## 8. Estado del proyecto

| Ítem evaluado                | Estado                |
| ---------------------------- | --------------------- |
| Ejecución sin errores        | ✅                     |
| Detección emocional          | ✅                     |
| Estado emocional persistente | ✅                     |
| Interacción HRI básica       | ✅                     |
| Buenas prácticas (Junior)    | ✅                     |
| Documentación                | ✅ Proyecto completado |

---

## 9 Retos opcionales (Bonus 🚀)

### Agregar una respuesta cuando el estado sea "neutro"

### Implementar transición emocional gradual (ej. triste → neutro → feliz)

### Contar el número de interacciones realizadas

### Separar el código en módulos (emotions.py, responses.py)

### Permitir detectar más de una emoción por frase
---
## 10. Conclusión
Este proyecto representa un avance sólido en Robótica Social, introduciendo el concepto de memoria emocional, fundamental para sistemas de interacción humano–robot.

El ejercicio refuerza:

### Lógica de programación

### Manejo de estado interno

### Diseño claro de funciones

### Respuestas empáticas simuladas

Este sistema sirve como base directa para futuros desarrollos como:

### Robots con personalidad

### Estados emocionales complejos

### Simulación de comportamiento social más realista

✅ Objetivos cumplidos para un nivel Junior.
