import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

#Login page
@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

#Registration page
@pytest.fixture(scope="function")
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

#Dashboard page
@pytest.fixture(scope="function")
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)

