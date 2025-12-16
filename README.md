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
git clone https://github.com/USUARIO/qa-login-form-playwright.git
```
```powershell
cd qa-login-form-playwright
```
```powershell
python -m venv .venv
```
```powershell
.\.venv\Scripts\Activate.ps1
```
```powershell
pip install -r requirements.txt
```
```powershell
python -m playwright install
```
```powershell
pytest
```
## ✅ Escenarios automatizados
- Login exitoso con credenciales válidas

## 📝 Notas de QA
- El test se ejecuta en modo headless por defecto
- Playwright interactúa con el navegador como un usuario real

## 📈 Mejoras futuras
- Implementar Page Object Model
- Agregar fixtures con conftest.py
- Automatizar escenarios negativos
- Captura de screenshots en fallos