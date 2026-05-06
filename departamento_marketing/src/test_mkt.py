import pandas as pd
import seaborn as sns
import requests
import sys
import os

def validacion_final():
    print("==============================================")
    print("   VALIDACIÓN: DEPARTAMENTO DE MARKETING")
    print("==============================================\n")

    # 1. VERIFICACIÓN DE VERSIONES
    print("[INFO] Verificando versiones del entorno:")
    print(f"- Python:   {sys.version.split()[0]}")
    print(f"- Pandas:   {pd.__version__}")
    print(f"- Seaborn:  {sns.__version__}")
    print(f"- Requests: {requests.__version__}")
    print("-" * 46)

    # 2. PRUEBA FUNCIONAL: Lectura de archivo CSV 
    print("\nArchivo")
    
    # Definimos la ruta relativa al archivo
    # El '..' le dice a Python: "Sal de la carpeta actual (src) y busca afuera"
    ruta_archivo = '../data/campanas.csv'
    
    if os.path.exists(ruta_archivo):
        # LEER EL ARCHIVO CSV DIRECTAMENTE
        df = pd.read_csv(ruta_archivo)
        
        # Calculamos la métrica (Costo por Conversión)
        df['costo_por_conv'] = df['presupuesto'] / df['conversiones']
        
        print(f"Archivo '{ruta_archivo}' procesado correctamente.\n")
        print(df)
        
        print("\n" + "=" * 46)
        print("✅ ENTORNO VALIDADO: Datos externos procesados con éxito.")
        print("==============================================")
    else:
        print(f"❌ ERROR: No se encontró el archivo '{ruta_archivo}'.")
        

if __name__ == "__main__":
    validacion_final()