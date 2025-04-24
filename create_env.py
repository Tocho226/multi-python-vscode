import os
import platform
import subprocess
import json

def main():
    version = input("¿Qué versión de Python quieres usar? (ej: 3.10): ").strip()
    env_name = f".venv{version.replace('.', '')}"

    print(f"\n🛠️  Creando entorno virtual: {env_name}")
    
    if platform.system() == "Windows":
        python_exe = f"py -{version}"
    else:
        python_exe = f"python{version}"

    try:
        subprocess.run([python_exe, "-m", "venv", env_name], check=True)
    except Exception as e:
        print(f"❌ Error creando el entorno: {e}")
        return

    print("✅ Entorno creado correctamente.\n📦 Configurando VSCode...")

    vscode_dir = ".vscode"
    os.makedirs(vscode_dir, exist_ok=True)

    if platform.system() == "Windows":
        interpreter_path = f"{env_name}\\Scripts\\python.exe"
    else:
        interpreter_path = f"{env_name}/bin/python"

    settings_path = os.path.join(vscode_dir, "settings.json")
    with open(settings_path, "w") as f:
        json.dump({
            "python.defaultInterpreterPath": interpreter_path
        }, f, indent=4)

    print(f"🎉 ¡Listo! VSCode está configurado con el intérprete: {interpreter_path}")

if __name__ == "__main__":
    main()
