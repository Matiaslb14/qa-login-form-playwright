import os
import re
import pytest
from playwright.sync_api import sync_playwright, Browser, Page

from utils.config import BASE_URL, LOGIN_PATH

def _slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9_-]+", "_", text)
    return text.strip("_")[:80] if text else "test"

@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL

@pytest.fixture(scope="session")
def login_path() -> str:
    return LOGIN_PATH

@pytest.fixture(scope="session")
def browser() -> Browser:
    headless_env = os.getenv("HEADLESS", "true").lower()
    headless = headless_env not in ("0", "false", "no")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser) -> Page:
    page = browser.new_page()
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Captura screenshot automático si falla el test.
    Se guarda en ./artifacts/screenshots/
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page is None:
            return

        os.makedirs("artifacts/screenshots", exist_ok=True)
        name = _slugify(item.nodeid.replace("::", "__"))
        path = f"artifacts/screenshots/{name}.png"
        try:
            page.screenshot(path=path, full_page=True)
        except Exception:
            # No rompemos el test por un fallo de screenshot
            pass
