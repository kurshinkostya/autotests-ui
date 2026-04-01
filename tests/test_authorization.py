import pytest
from playwright.sync_api import expect, sync_playwright, Page
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authrization
@pytest.mark.parametrize(
    'email, password',
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str) -> Page: 
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
    
    
    
    