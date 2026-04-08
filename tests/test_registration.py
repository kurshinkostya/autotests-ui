import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    
    email = "user.name@gmail.com"
    username = "username"
    password = "password"
    
    registration_page.form.fill(email, username, password)
    registration_page.form.check_visible(email, username, password)
    
    registration_page.form.submit()
    
    dashboard_page.toolbar.check_visible()