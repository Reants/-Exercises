# 🤖 Robot Social Básico con Detección Emocional (Texto)

## 1. Descripción del ejercicio
En este proyecto crearás un **simulador simple de un robot social** que interactúa con una persona a través de texto.

El robot:
- Recibe una frase escrita por el usuario
- Identifica una emoción básica a partir de palabras clave
- Responde de forma empática según la emoción detectada

Este ejercicio **no usa inteligencia artificial avanzada**, sino **lógica básica**, simulando cómo un robot social comienza a interpretar emociones humanas.

---

## 2. Objetivo de aprendizaje
Al finalizar este ejercicio serás capaz de:

- Aplicar **pensamiento lógico** para simular detección emocional
- Usar estructuras básicas de Python (`if`, funciones, diccionarios)
- Separar responsabilidades en funciones
- Comprender el flujo básico de una **interacción humano–robot (HRI)**
- Escribir código claro, legible y bien estructurado

---

## 3. Tecnologías usadas
- Python 3.x
- Consola / Terminal

---

## 4. Requisitos previos
- Conocimientos básicos de Python:
  - Variables
  - Condicionales (`if / elif / else`)
  - Funciones
  - Diccionarios (nivel introductorio)

> No se requieren librerías externas.

---

## 5. Instrucciones paso a paso

### 🧩 Etapa 1: Preparar el entorno
1. Crea una carpeta para el proyecto
2. Dentro de ella, crea un archivo principal en Python
3. Asegúrate de poder ejecutar el archivo desde la terminal

---

### 🧠 Etapa 2: Entrada del usuario
- Solicita al usuario que escriba cómo se siente o qué le pasó
- Guarda esa frase en una variable
- Normaliza el texto (por ejemplo, todo en minúsculas)

---

### 😊 Etapa 3: Detección emocional básica
- Define al menos **3 emociones**:
  - Alegría
  - Tristeza
  - Enojo
- Asocia cada emoción a una lista de palabras clave
- Analiza el texto del usuario para detectar si alguna palabra clave aparece

---

### 🤖 Etapa 4: Respuesta empática del robot
- Crea una respuesta diferente para cada emoción
- La respuesta debe sonar:
  - Respetuosa
  - Empática
  - Natural (como un robot social básico)
- Si no se detecta ninguna emoción, usa una respuesta neutral

---

### 🔁 Etapa 5: Flujo completo
- Integra todo en un flujo claro:
  1. El robot saluda
  2. El usuario escribe
  3. El robot detecta emoción
  4. El robot responde

---

## 6. Estructura sugerida del proyecto

```text
robot-social-basico/
│
├── main.py
├── emotions.py        # (opcional) lógica de detección emocional
├── responses.py       # (opcional) respuestas del robot
└── README.md

---

## 7. Correcciones aplicadas al código

Las siguientes mejoras fueron realizadas durante la revisión final del proyecto:

| Área | Corrección aplicada |
|----|---------------------|
| Ejecución del programa | Llamada correcta a la función `main()` |
| Lógica de detección | Eliminación del uso de índices para comparar emociones |
| Detección emocional | Comparación directa de palabras del usuario con listas emocionales |
| Operadores lógicos | Uso correcto del operador `and` en condiciones |
| Variables | Evitar sobrescribir funciones nativas como `input` |
| Normalización de texto | Conversión del texto del usuario a minúsculas |
| Ortografía | Corrección de palabras clave emocionales (ej. `irritado`) |

---

## 8. Estado del proyecto

| Ítem evaluado | Estado |
|-------------|--------|
| Ejecución sin errores | ✅ |
| Detección emocional básica | ✅ |
| Flujo humano–robot (HRI) | ✅ |
| Buenas prácticas (nivel Junior) | ✅ |
| Documentación (README) | ✅ |
| Entrega del proyecto | ✅ Proyecto completado |

---

## 9. Retos opcionales (Bonus 🚀)

Para continuar mejorando este proyecto, se proponen los siguientes retos:

- Implementar **memoria emocional básica** (recordar la última emoción detectada)
- Detectar **múltiples emociones** en una sola frase
- Ajustar el saludo del robot según interacciones previas
- Usar valores booleanos (`True / False`) en lugar de `1 / 0`
- Separar completamente la lógica en módulos (`emotions.py`, `responses.py`)
- Contar el número de interacciones realizadas

---

## 10. Conclusión

Este proyecto representa un **primer acercamiento sólido a la robótica social**, aplicando:

- Lógica básica para detección emocional
- Interacción humano–robot mediante texto
- Respuestas empáticas simuladas
- Código claro, funcional y mantenible

El sistema desarrollado sirve como **base para proyectos más avanzados**, como:
- Robots con memoria emocional
- Integración con sensores o reconocimiento de voz
- Sistemas de detección emocional más complejos

Este trabajo cumple correctamente los objetivos propuestos para un **nivel Junior**.
