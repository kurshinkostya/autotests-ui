from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


# class DashboardToolbarViewComponent(BaseComponent):
#     def __init__(self, page: Page):
#         super().__init__(page)

#         self.title = page.get_by_test_id('dashboard-toolbar-title-text')

#     def check_visible(self):
#         expect(self.title).to_be_visible()
#         expect(self.title).to_have_text("Dashboard")

from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Dashboard title')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Dashboard")