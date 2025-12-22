# QA Login Automation – Playwright + Pytest

## 📌 Descripción
Proyecto de **QA Automation** enfocado en la validación del **flujo de login** de una aplicación web utilizando **Playwright** y **Pytest**.  
El objetivo es simular la interacción real de un usuario y verificar el comportamiento esperado ante un inicio de sesión exitoso, sirviendo como primer acercamiento a la automatización de pruebas web.

## ⭐ Características / Features Clave
- Automatización de pruebas web con **Playwright**
- Ejecución de tests en navegador **Chromium**
- Simulación de interacción real de usuario
- Estructura simple y directa orientada a aprendizaje inicial
- Ejecución en modo **headless**

## 🧪 Qué se está probando
- Formulario de login
- Flujo de autenticación con credenciales válidas
- Visualización de mensaje o estado de éxito posterior al login

## 🛠 Stack Tecnológico
- **Python**
- **Pytest**
- **Playwright**
- Chromium (modo headless)

## 📂 Estructura del Proyecto
```text
qa-login-form-playwright/
├── tests/
│  └── test_login.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```
## ▶️ Cómo ejecutar el proyecto
```powershell
# Clonar el repositorio e ingresar al proyecto
git clone https://github.com/Matiaslb14/qa-login-form-playwright.git
cd qa-login-form-playwright

# Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias y navegadores
pip install -r requirements.txt
python -m playwright install

# Ejecutar los tests
pytest
```
## ✅ Escenarios automatizados
- Login exitoso con credenciales válidas

## 🧠 Decisiones técnicas
- Se utiliza **Playwright** por su velocidad y confiabilidad en automatización web moderna.
- El test se ejecuta en modo **headless** para facilitar su ejecución en distintos entornos.
- Se utiliza un sitio público de pruebas con credenciales conocidas para evitar dependencias externas.

## 📊 Reportes / Evidencia (cuando aplique)
- La ejecución de los tests se valida mediante la salida estándar de **Pytest**.
- No se incluyen evidencias visuales al tratarse de un proyecto introductorio.

## 📈 Mejoras futuras
- Implementar **Page Object Model (POM)**
- Agregar fixtures con conftest.py
- Automatizar escenarios negativos
- Incorporar captura automática de screenshots en fallos