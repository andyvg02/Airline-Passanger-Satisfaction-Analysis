import os

# Ruta donde se creará la carpeta .streamlit
folder_path = ".streamlit"
file_path = os.path.join(folder_path, "config.toml")

# Crear carpeta si no existe
os.makedirs(folder_path, exist_ok=True)

# Contenido del archivo de configuración
config_content = """
[theme]
primaryColor="#1E88E5"
backgroundColor="#F7F9FC"
secondaryBackgroundColor="#FFFFFF"
textColor="#1A1A1A"
font="sans serif"
"""

# Crear el archivo
with open(file_path, "w", encoding="utf-8") as f:
    f.write(config_content.strip())

print("Archivo .streamlit/config.toml creado correctamente.")