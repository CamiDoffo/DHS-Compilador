import os
import shutil
import subprocess

# Rutas
path_grammar = "src/main/antlr4/compiladores.g4"
path_output = "src/main/python"

print("--- 1. Limpiando archivos viejos de Python ---")
files_to_remove = [
    "compiladoresLexer.py", "compiladoresParser.py", 
    "compiladoresListener.py", "compiladoresVisitor.py"
]
for f in files_to_remove:
    full_path = os.path.join(path_output, f)
    if os.path.exists(full_path):
        os.remove(full_path)
        print(f"Eliminado: {f}")

# Limpiar cache y tokens
for root, dirs, files in os.walk(path_output):
    for f in files:
        if f.endswith(".tokens") or f.endswith(".interp"):
            os.remove(os.path.join(root, f))
    for d in dirs:
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d))

print("\n--- 2. Regenerando Parser con ANTLR ---")
cmd = f"antlr4 -Dlanguage=Python3 -visitor -listener -o {path_output} {path_grammar}"
result = subprocess.run(cmd, shell=True)

if result.returncode == 0:
    print("✅ Parser regenerado con éxito.")
    print("\n--- 3. Ejecutando Pruebas ---")
    subprocess.run(f"py -B src/main/python/App.py input/prueba_final.txt", shell=True)
else:
    print("❌ Error al regenerar el parser. Verifica que tengas Java y ANTLR instalados.")