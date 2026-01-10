import pytest
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_snippet",
    [
        ("tomsmith", "wrongpassword", "Your password is invalid!"),
        ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
        ("", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "", "Your password is invalid!"),
    ],
)
def test_login_negative_cases(page, base_url, login_path, username, password, expected_snippet):
    login = LoginPage(page)
    login.open(base_url, login_path)

    login.login(username, password)

    msg = login.flash_message()
    assert expected_snippet in msg

@pytest.mark.regression
def test_login_input_is_handled_safely(page, base_url, login_path):
    """
    Security-aware check (QA perspective):
    - Inputs raros/largos no deben romper el flujo.
    - Debe retornar error controlado (no crash/blank page).
    """
    login = LoginPage(page)
    login.open(base_url, login_path)

    weird_username = "tomsmith" + ("<script>alert(1)</script>" * 5)
    weird_password = "x" * 300

    login.login(weird_username, weird_password)

    msg = login.flash_message()
    # Cualquier mensaje de invalidación controlada es aceptable.
    assert "invalid" in msg.lower()
