# Changelog

Todos los cambios relevantes de este proyecto se documentan aquí.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y [Versionado Semántico](https://semver.org/lang/es/).

## [1.1.0] - 2026-10-26

### 🔧 Mantenimiento

- Verificación completa: los 4 notebooks (EDA, boosting, no supervisado y extra) se ejecutan de principio a fin sin errores con las versiones fijadas en `requirements.txt`.
- Pruebas automatizadas: integridad del dataset (10.000 clientes, target binario, IDs únicos) y ejecución de los notebooks 1 y 4.
- Flujo de CI que corre las pruebas en cada cambio.
- Licencia MIT e insignias en el README.
