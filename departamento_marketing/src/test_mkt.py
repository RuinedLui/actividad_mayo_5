import pandas as pd
import seaborn as sns
import requests
import sys
import io

def validacion_final():
    print("==============================================")
    print("   VALIDACIÓN: DEPARTAMENTO DE MARKETING")
    print("==============================================\n")

    # 1. VERIFICACIÓN DE VERSIONES (Requisito de Rúbrica)
    print("[INFO] Verificando versiones del entorno:")
    print(f"- Python:   {sys.version.split()[0]}")
    print(f"- Pandas:   {pd.__version__}")
    print(f"- Seaborn:  {sns.__version__}")
    print(f"- Requests: {requests.__version__}")
    print("-" * 46)

    # 2. PRUEBA FUNCIONAL: Lectura de CSV Ficticio
    print("\n[TEST] Ejecutando análisis de campaña (Pandas):")
    
    csv_marketing = """campaña,clics,conversiones,presupuesto
Facebook_Ads,1200,45,150
Google_Search,2500,110,300
Instagram_Influencer,800,30,100
"""
    # Leemos el string como si fuera un archivo .csv
    df = pd.read_csv(io.StringIO(csv_marketing))
    
    # Calculamos una métrica rápida (Costo por Conversión)
    df['costo_por_conv'] = df['presupuesto'] / df['conversiones']
    
    print(df)
    
    # 3. RESULTADO
    print("\n" + "=" * 46)
    print("✅ ENTORNO VALIDADO:")
    print("==============================================")

if __name__ == "__main__":
    validacion_final()