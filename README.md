![FinanceGuard](docs/cover.svg)

# FinanceGuard

**Modelos y escenarios económicos para estudiar abandono de clientes bancarios.**

HENRY · MÓDULO 4 · PROYECTO INTEGRADOR · Python · scikit-learn · Stacking · Power BI

[Portafolio](https://dodysalim.github.io/) · [Caso y alcance](docs/PORTFOLIO_CASE.md) · [Verificación](docs/VALIDATION.md)

## La pregunta

¿Cómo comparar modelos de churn y seleccionar un umbral considerando falsos positivos y costos de retención?

## Qué puedes revisar

- EDA y regresión logística; comparación de boosting y stacking.
- PCA, clustering y análisis de segmentos.
- Matriz de costos y escenarios de retención; tres páginas Power BI.

## Inicio local

Usa Python 3.11 o 3.12 en un entorno independiente. Desde la raíz:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Después de configurar los datos:

```bash
python -m jupyter lab
```

## Datos y configuración

Dataset Churn_Modelling incluido, con 10.000 registros. Abre los notebooks desde la carpeta notebooks y sigue el orden numerado.

## Power BI · PC y móvil

[Archivos e instrucciones](powerbi/README.md). Descarga el repositorio completo y abre `powerbi/Abrir-PowerBI.bat` en Windows; después pulsa **Actualizar**. Incluye A4 horizontal a tamaño real (100 %) y diseño móvil vertical. El archivo `.pbip` necesita sus carpetas Report, SemanticModel y data.

## Recorrido por el código

| Ruta | Qué contiene |
| --- | --- |
| [notebooks/](notebooks/) | EDA, modelos, segmentación y costos |
| [data/Churn_Modelling.csv](data/Churn_Modelling.csv) | Datos académicos originales |
| [images/](images/) | Figuras publicadas |

## Comprobación y alcance

Notebook 1 (EDA y regresión logística) ejecutado completo: 20 celdas de código sin errores. Código de los otros notebooks revisado sintácticamente y dataset comprobado. Las métricas históricas publicadas pertenecen a las ejecuciones guardadas; no se reentrenó el stacking en esta revisión.

La retención y el ROI son escenarios con supuestos, no ingresos recuperados observados. El dashboard Power BI analiza Exited observado, no probabilidades nuevas del modelo.

## Autoría

Proyecto integrador del módulo 4 de Henry, localizado en la carpeta M4. Dody Salim Dueñas Remache.

[Documentación anterior](docs/ORIGINAL_README.md), conservada como referencia histórica.
