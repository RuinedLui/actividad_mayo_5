import numpy as np
import pandas as pd

# Verificacion de dependencias - Departamento ML
print("------------------------------------------")
print("  Entorno ML - Verificacion de librerias  ")
print("------------------------------------------")
print(f"[OK] numpy   version: {np.__version__}")
print(f"[OK] pandas  version: {pd.__version__}")

# Prueba basica
datos = np.array([5, 10, 15, 20, 25])
df = pd.DataFrame(datos, columns=["muestra"])
print(f"\nPromedio de prueba: {df['muestra'].mean()}")
print("Entorno listo para usar.")