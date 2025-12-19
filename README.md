# QA Login Automation – Playwright + Pytest

## 📌 Descripción
Proyecto de QA Automation que valida el flujo de login de una aplicación web utilizando Playwright y Pytest.  
Simula la interacción real de un usuario y verifica el resultado esperado tras un inicio de sesión exitoso.

## 🧪 Qué se está probando
- Formulario de login
- Flujo de autenticación con credenciales válidas
- Mensaje de éxito posterior al login

## 🛠 Stack Tecnológico
- Python
- Pytest
- Playwright
- Chromium (modo headless)

## 📂 Estructura del Proyecto
```
qa-login-form-playwright/
├── tests/
│ └── test_login.py
├── pytest.ini
├── requirements.txt
└── .gitignore
```
- `tests/`: contiene los tests automatizados
- `pytest.ini`: configuración global de Pytest
- `requirements.txt`: dependencias del proyecto
- `.gitignore`: archivos y carpetas ignoradas por Git

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

## 📝 Notas de QA
- El test se ejecuta en modo headless por defecto
- Playwright interactúa con el navegador como un usuario real
- Se utiliza un sitio público de pruebas con credenciales conocidas

## 📈 Mejoras futuras
- Implementar Page Object Model
- Agregar fixtures con conftest.py
- Automatizar escenarios negativos
- Captura de screenshots en fallos
