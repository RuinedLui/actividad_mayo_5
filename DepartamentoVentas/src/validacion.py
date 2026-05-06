import pandas as pd
import numpy as np

print("=== Validación de entorno - Departamento Ventas ===")
print(f"pandas: {pd.__version__}")
print(f"numpy:  {np.__version__}")
print()

# Simulacion de datos de ventas
productos = ["Laptop", "Monitor", "Teclado", "Mouse", "Auriculares"]
ventas = np.array([150, 89, 230, 310, 175])

df = pd.DataFrame({
    "producto": productos,
    "unidades_vendidas": ventas
})

total = df["unidades_vendidas"].sum()
promedio = df["unidades_vendidas"].mean()
mas_vendido = df.loc[df["unidades_vendidas"].idxmax(), "producto"]

print(df.to_string(index=False))
print()
print(f"Total vendido:     {total} unidades")
print(f"Promedio:          {promedio:.1f} unidades")
print(f"Producto estrella: {mas_vendido}")
print()
print("Entorno Ventas operativo ✓")