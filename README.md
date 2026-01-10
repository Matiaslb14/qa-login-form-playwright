# QA Login Automation – Playwright + Pytest
[![CI](https://github.com/Matiaslb14/qa-login-form-playwright/actions/workflows/ci.yml/badge.svg)](https://github.com/Matiaslb14/qa-login-form-playwright/actions)
## 📌 Descripción
Proyecto de **QA Automation** enfocado en la validación del **flujo de autenticación** de una aplicación web, utilizando **Playwright** y **Pytest**.

El objetivo es automatizar un **flujo crítico de negocio**, aplicando buenas prácticas de la industria como **Page Object Model (POM)**, **fixtures reutilizables**, **escenarios negativos**, **ejecución por marcadores** y **captura automática de evidencias en fallos**, asegurando estabilidad tanto en ejecución local como en **CI/CD**.

Se utiliza una aplicación pública de pruebas para simular un entorno real sin dependencias externas.

## ⭐ Características / Features Clave
- Automatización de UI con **Playwright**
- Arquitectura basada en **Page Object Model (POM)**
- Uso de **fixtures** para setup y teardown
- Separación de tests:
    - **Smoke** (críticos y rápidos)
    - **Regression** (escenarios negativos y validaciones extendidas)
- Ejecución en modo **headless**
- **Captura automática de screenshots** en caso de fallo
- **Integración continua con GitHub Actions**
- Enfoque en **calidad, mantenibilidad y estabilidad**

## 🧪 Qué se prueba
- Autenticación exitosa (happy path)
- Escenarios negativos:
    - Usuario inválido
    - Password inválida
    - Campos vacíos 
- Comportamiento ante inputs anómalos (security-aware checks)
- Mensajes de error controlados y consistentes

## 🔐 Security-aware checks (QA perspective)

Desde una perspectiva de QA (no pentesting), se validan:
- Manejo seguro de inputs inesperados o largos
- Ausencia de crashes ante datos anómalos
- Mensajes de error controlados (sin filtración de información sensible)
- Comportamiento estable del flujo de autenticación

## 🛠 Stack Tecnológico
- **Python**
- **Pytest**
- **Playwright**
- **Chromium**
- **GitHub Actions**

## 📂 Estructura del Proyecto
```text
qa-login-form-playwright/
├── pages/
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login_positive.py
│   └── test_login_negative.py
├── utils/
│   └── config.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── pytest.ini
├── requirements.txt
└── README.md
```
## ▶️ Cómo ejecutar el proyecto
### Ejecución local
```powershell
# Clonar el repositorio
git clone https://github.com/Matiaslb14/qa-login-form-playwright.git
cd qa-login-form-playwright

# Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
python -m playwright install chromium

# Ejecutar todos los tests
pytest
```
### Ejecutar por tipo de prueba
```powershell
# Smoke tests (rápidos, críticos)
pytest -m smoke

# Regression tests
pytest -m regression
```
## 🤖 CI – GitHub Actions
- Los tests se ejecutan automáticamente en cada **push** y **pull request**
- Se ejecutan en modo **headless**
- En caso de fallo, se generan **screenshots automáticos** como evidencia
- El pipeline actúa como validación de integración continua

## 🧠 Decisiones técnicas
- Se utiliza **Playwright** por su velocidad, estabilidad y soporte moderno para UI testing.
- Se implementa **POM** para mejorar mantenibilidad y escalabilidad.
- Los tests se dividen por marcadores para optimizar tiempos de ejecución.
- Se prioriza **calidad del diseño de tests** por sobre cantidad.
- No se utilizan frameworks innecesarios para mantener el foco en QA Automation.

## 📌 Alcance del proyecto

**Incluye**
- Automatización de UI
- Escenarios positivos y negativos
- Evidencia automática en fallos
- CI/CD

**No incluye**
- Backend propio
- Pruebas de carga
- Pentesting

📈 Próximos pasos

- Reportes HTML automáticos en CI
- Ejecución paralela de tests
- Extensión del flujo a logout y recuperación de sesión