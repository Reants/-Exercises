from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from tools import TOOLS, list_files_in_directory, read_file, edit_file, delete_file

load_dotenv()
cliente = genai.Client(api_key=os.getenv("API_KEY"))

history = []
system_prompt = "Eres un asistente útil y amigable. Responde a las preguntas de los usuarios de manera clara y concisa."

while True:
    user_input = input("Usuario: ")

    if not user_input:
        continue

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("Chatbot: ¡Hasta luego!")
        break

    history.append(types.Content(
        role="user",
        parts=[types.Part(text=user_input)]
    ))

    while True:
        response = cliente.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=TOOLS  # ← usa la lista centralizada
            )
        )

        history.append(response.candidates[0].content)
        part = response.candidates[0].content.parts[0]

        if part.function_call:
            fn_name = part.function_call.name
            fn_args = dict(part.function_call.args)

            print(f"  → Herramienta: {fn_name}")
            print(f"  → Argumentos: {fn_args}")

            if fn_name == "list_files_in_directory":
                result = list_files_in_directory(**fn_args)
            elif fn_name == "read_file":
                result = read_file(**fn_args)
            elif fn_name == "edit_file":
                result = edit_file(**fn_args)
            elif fn_name == "delete_file":
                result = delete_file(**fn_args)

            history.append(types.Content(
                role="user",
                parts=[types.Part(
                    function_response=types.FunctionResponse(
                        name=fn_name,
                        response=result
                    )
                )]
            ))

        else:
            print(f"Chatbot: {response.text}")
            break