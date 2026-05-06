"""
Modulo principal de calculo NPS
Departamento de Satisfaccion del Cliente
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def cargar_datos(ruta_csv: str) -> pd.DataFrame:
    """Carga el archivo CSV de encuestas."""
    df = pd.read_csv(ruta_csv)
    print(f"Datos cargados: {len(df)} registros desde '{ruta_csv}'")
    return df


def clasificar_respuestas(df: pd.DataFrame, col: str = "puntuacion") -> pd.DataFrame:
    """Agrega columna de categoria NPS."""
    def _clasificar(p):
        if p >= 9:   return "Promotor"
        elif p >= 7: return "Pasivo"
        else:        return "Detractor"
    df = df.copy()
    df["categoria"] = df[col].apply(_clasificar)
    return df


def calcular_nps(df: pd.DataFrame) -> float:
    """Calcula el NPS a partir de un DataFrame clasificado."""
    total       = len(df)
    promotores  = (df["categoria"] == "Promotor").sum()
    detractores = (df["categoria"] == "Detractor").sum()
    return round((promotores - detractores) / total * 100, 2)


def reporte_nps(df: pd.DataFrame) -> None:
    """Imprime un reporte resumen del NPS."""
    nps    = calcular_nps(df)
    counts = df["categoria"].value_counts()
    total  = len(df)

    print("\n" + "=" * 40)
    print("  REPORTE NPS")
    print("=" * 40)
    for cat in ["Promotor", "Pasivo", "Detractor"]:
        n = counts.get(cat, 0)
        print(f"  {cat:<12}: {n:>4}  ({n/total*100:5.1f}%)")
    print(f"\n  NPS Final: {nps}")
    print("=" * 40)


def graficar_distribucion(df: pd.DataFrame, guardar: bool = False) -> None:
    """Genera grafico de distribucion de puntuaciones."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Analisis NPS - Satisfaccion del Cliente", fontsize=14)

    # Histograma de puntuaciones
    sns.countplot(data=df, x="puntuacion", palette="RdYlGn", ax=axes[0])
    axes[0].set_title("Distribucion de Puntuaciones")
    axes[0].set_xlabel("Puntuacion (0-10)")
    axes[0].set_ylabel("Cantidad")

    # Pie de categorias
    counts = df["categoria"].value_counts()
    colors = {"Promotor": "#4CAF50", "Pasivo": "#FFC107", "Detractor": "#F44336"}
    axes[1].pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        colors=[colors[c] for c in counts.index],
        startangle=90,
    )
    axes[1].set_title("Segmentacion de Clientes")

    plt.tight_layout()
    if guardar:
        plt.savefig("data/nps_distribucion.png", dpi=150)
        print("Grafico guardado en data/nps_distribucion.png")
    plt.show()


if __name__ == "__main__":
    # Demo rapida con datos sinteticos
    np.random.seed(0)
    datos = pd.DataFrame({
        "cliente_id": range(1, 201),
        "puntuacion": np.random.choice(range(11), size=200,
                                       p=[0.02,0.02,0.03,0.03,0.05,
                                          0.05,0.05,0.10,0.15,0.25,0.25])
    })
    datos = clasificar_respuestas(datos)
    reporte_nps(datos)
    graficar_distribucion(datos)