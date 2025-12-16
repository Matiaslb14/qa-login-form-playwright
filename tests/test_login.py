from playwright.sync_api import sync_playwright

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator('button[type="submit"]').click()

        flash = page.locator("#flash")
        flash.wait_for()

        assert "You logged into a secure area!" in flash.inner_text()

        browser.close()