# Departamento de Marketing: Gestión de Entornos

Este proyecto demuestra la configuración profesional de un entorno aislado utilizando **Conda** para el análisis de datos de marketing.

## 🛠️ Requerimientos Técnicos
- **Python:** 3.10
- **Librerías principales:** Pandas, Seaborn, Requests

## 🚀 Guía de Reproducción
Para reconstruir este entorno desde cero, ejecute en su terminal:

1. **Crear entorno desde archivo:
   `conda env create -f environment.yml -n mkt_Reconstruido`

2. **Activar:**
   `conda activate mkt_Reconstruido`


## ⚖️ Resolución de Conflictos
Se aplicó la gestión de dependencias mediante el SAT Solver de Conda, asegurando la compatibilidad entre las versiones de `pandas` y `seaborn`. El sistema resuelve automáticamente el árbol de dependencias para evitar el Dependency Hell