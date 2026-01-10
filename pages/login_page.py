from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator('button[type="submit"]')
        self.flash = page.locator("#flash")

    def open(self, base_url: str, login_path: str = "/login") -> None:
        self.page.goto(f"{base_url}{login_path}", wait_until="domcontentloaded")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def flash_message(self) -> str:
        # Herokuapp flash incluye un "×" al final; limpiamos espacios.
        self.flash.wait_for(state="visible")
        return self.flash.inner_text().strip()
