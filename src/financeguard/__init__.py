"""FinanceGuard: predicción de abandono bancario como paquete reutilizable.

Módulos (una responsabilidad cada uno):
    config      → rutas, columnas y semillas
    data        → carga y partición estratificada
    features    → preprocesamiento (escalado + one-hot)
    models      → registro de modelos (fábrica extensible)
    evaluation  → métricas y tabla comparativa
    costs       → matriz de costos y umbral óptimo de negocio
"""
__version__ = "1.2.0"
