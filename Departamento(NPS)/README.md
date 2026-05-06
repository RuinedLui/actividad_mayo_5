# Departamento de Satisfacción del Cliente — NPS

## Descripción
Entorno de análisis para calcular y visualizar el Net Promoter Score (NPS)
de clientes, detectar tendencias y segmentar respuestas.

## Librerías principales
| Librería    | Versión | Uso                              |
|-------------|---------|----------------------------------|
| pandas      | 2.1.4   | Manipulación de datos            |
| numpy       | 1.26.4  | Cálculos numéricos               |
| matplotlib  | 3.8.2   | Visualizaciones                  |
| seaborn     | 0.13.2  | Gráficos estadísticos            |
| scipy       | 1.12.0  | Análisis estadístico             |
| openpyxl    | 3.1.2   | Lectura/escritura de Excel       |

---

## Configuración con venv (pip)

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno
source venv/bin/activate        # Linux / Mac
# venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar instalación
python src/validar_entorno.py
```

## Configuración con conda

```bash
# 1. Crear entorno desde archivo
conda env create -f environment.yml

# 2. Activar entorno
conda activate nps_env

# 3. Verificar instalación
python src/validar_entorno.py
```

## Desactivar entorno

```bash
deactivate          # venv
conda deactivate    # conda
```

## Reproducir en otra máquina

```bash
# Con pip
pip install -r requirements.txt

# Con conda
conda env create -f environment.yml
conda activate nps_env
```

## Estructura del proyecto

```
nps_proyecto/
├── venv/                   # Entorno virtual (no subir a Git)
├── src/
│   ├── validar_entorno.py  # Script de validación
│   └── calcular_nps.py     # Lógica principal de NPS
├── notebooks/
│   └── analisis_nps.ipynb  # Notebook de análisis
├── data/
│   └── encuestas_demo.csv  # Datos de ejemplo
├── requirements.txt
├── environment.yml
└── README.md
```

## Concepto NPS
- **Promotores** (9–10): clientes leales
- **Pasivos**   (7–8):  satisfechos pero vulnerables
- **Detractores** (0–6): insatisfechos

**NPS = % Promotores − % Detractores**