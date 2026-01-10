import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_success(page, base_url, login_path):
    login = LoginPage(page)
    login.open(base_url, login_path)

    login.login("tomsmith", "SuperSecretPassword!")

    msg = login.flash_message()
    assert "You logged into a secure area!" in msg
