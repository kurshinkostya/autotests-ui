import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture       
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(browser):
    content = browser.new_context()
    page = content.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')
    
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')
    
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')
    
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    
    content.storage_state(path='browser-state.json')
    

@pytest.fixture
def chromium_page_with_state(
    initialize_browser_state,
    browser
):
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page