"""
Script de validacion del entorno
Departamento de Satisfaccion del Cliente (NPS)
"""
import sys
import importlib

LIBRERIAS = [
    "pandas",
    "numpy",
    "seaborn",
    "scipy",
    "openpyxl",
]

def verificar_librerias():
    print("=" * 55)
    print("  VALIDACION DE ENTORNO - NPS")
    print("=" * 55)
    print(f"Python: {sys.version}\n")
    print(f"{'Libreria':<15} {'Version':<12} {'Estado'}")
    print("-" * 45)

    errores = []
    for nombre in LIBRERIAS:
        try:
            mod = importlib.import_module(nombre)
            version = getattr(mod, "__version__", "N/A")
            print(f"{nombre:<15} {version:<12} OK")
        except ImportError:
            print(f"{nombre:<15} {'---':<12} NO INSTALADA")
            errores.append(nombre)

    print("-" * 45)
    if errores:
        print(f"\nFaltan {len(errores)} libreria(s): {', '.join(errores)}")
        print("   Ejecuta: pip install -r requirements.txt")
        sys.exit(1)
    else:
        print("\nTodas las librerias estan instaladas correctamente.")

def prueba_funcional():
    print("\n--- Prueba funcional NPS ---")
    import pandas as pd
    import numpy as np

    # Simular respuestas de encuesta (escala 0-10)
    np.random.seed(42)
    respuestas = np.random.choice(range(11), size=100,
                                  p=[0.02,0.02,0.03,0.03,0.05,
                                     0.05,0.05,0.10,0.15,0.25,0.25])

    df = pd.DataFrame({"puntuacion": respuestas})

    def clasificar(p):
        if p >= 9:   return "Promotor"
        elif p >= 7: return "Pasivo"
        else:        return "Detractor"

    df["categoria"] = df["puntuacion"].apply(clasificar)

    total        = len(df)
    promotores   = (df["categoria"] == "Promotor").sum()
    detractores  = (df["categoria"] == "Detractor").sum()
    nps          = round((promotores - detractores) / total * 100, 2)

    print(f"  Total encuestas : {total}")
    print(f"  Promotores      : {promotores} ({promotores/total*100:.1f}%)")
    print(f"  Pasivos         : {(df['categoria']=='Pasivo').sum()}")
    print(f"  Detractores     : {detractores} ({detractores/total*100:.1f}%)")
    print(f"\n  NPS = {nps}")

    if nps > 50:
        print("  Clasificacion: Excelente")
    elif nps > 0:
        print("  Clasificacion: Positivo")
    else:
        print("  Clasificacion: Necesita mejora")

    print("\nPrueba funcional completada con exito.")

if __name__ == "__main__":
    verificar_librerias()
    prueba_funcional()