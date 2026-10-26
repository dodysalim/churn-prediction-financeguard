# Changelog

Todos los cambios relevantes de este proyecto se documentan aquí.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y [Versionado Semántico](https://semver.org/lang/es/).

## [1.2.0] - 2026-10-26

### 🔧 Mantenimiento

- **Nuevo paquete `src/financeguard/`:** la carga, partición, preprocesamiento, modelos, métricas y matriz de costos que se repetían en los 4 notebooks ahora son módulos reutilizables con una responsabilidad cada uno.
- **SOLID:** registro de modelos extensible con `register()` (abierto/cerrado), costos de negocio como objeto inmutable `BusinessCosts` y funciones puras para el umbral óptimo.
- **`train.py`:** compara modelos y elige el umbral de negocio desde la terminal; reproduce exactamente los resultados del notebook 4 (umbral 0,10; $58.400 → $111.700 en prueba).
- 5 pruebas nuevas del paquete (8 en total); CI ejecuta además `train.py`.
- Los notebooks se conservan sin cambios como narrativa del análisis.

## [1.1.0] - 2026-10-26

### 🔧 Mantenimiento

- Verificación completa: los 4 notebooks (EDA, boosting, no supervisado y extra) se ejecutan de principio a fin sin errores con las versiones fijadas en `requirements.txt`.
- Pruebas automatizadas: integridad del dataset (10.000 clientes, target binario, IDs únicos) y ejecución de los notebooks 1 y 4.
- Flujo de CI que corre las pruebas en cada cambio.
- Licencia MIT e insignias en el README.
