import os

def list_files_in_directory(directory: str = ".") -> dict:
    """Lista los archivos en un directorio.

    Args:
        directory: Ruta del directorio a listar. Por defecto el directorio actual.
    """
    print("⚙️ Herramienta ejecutada: list_files_in_directory")
    try:
        files = os.listdir(directory)
        return {"files": list(files)}
    except Exception as e:
        return {"error": str(e)}

def read_file(path: str) -> dict:
    """Lee el contenido de un archivo.

    Args:
        path: Ruta del archivo a leer.
    """
    print("⚙️ Herramienta ejecutada: read_file")
    try:
        with open(path, encoding="utf-8") as f:
            return {"content": f.read()}
    except Exception as e:
        return {"error": str(e)}

def edit_file(path: str, new_text: str, prev_text: str = "") -> dict:
    """Edita o crea un archivo. Si el archivo existe, reemplaza prev_text por new_text.
    Si no existe, lo crea con new_text.

    Args:
        path: Ruta del archivo a editar o crear.
        new_text: Texto nuevo que reemplazará a prev_text, o contenido del archivo nuevo.
        prev_text: Texto a buscar y reemplazar. Dejar vacío si se crea archivo nuevo.
    """
    print("⚙️ Herramienta ejecutada: edit_file")
    try:
        if os.path.exists(path) and prev_text:
            content = read_file(path)["content"]
            if prev_text not in content:
                return {"error": f"Texto '{prev_text}' no encontrado en el archivo"}
            content = content.replace(prev_text, new_text)
        else:
            dir_name = os.path.dirname(path)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            content = new_text

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        action = "editado" if os.path.exists(path) and prev_text else "creado"
        return {"result": f"Archivo {path} {action} exitosamente"}
    except Exception as e:
        return {"error": str(e)}

def delete_file(path: str) -> dict:
    """Elimina un archivo del sistema.

    Args:
        path: Ruta del archivo a eliminar.
    """
    print("⚙️ Herramienta ejecutada: delete_file")
    try:
        if not os.path.exists(path):
            return {"error": f"El archivo {path} no existe"}
        os.remove(path)
        return {"result": f"Archivo {path} eliminado exitosamente"}
    except Exception as e:
        return {"error": str(e)}

# Lista centralizada de herramientas para importar fácilmente
TOOLS = [list_files_in_directory, read_file, edit_file, delete_file]