from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


# class EmptyViewComponent(BaseComponent):
#     def __init__(self, page: Page, identifier: str):
#         super().__init__(page) 
        
#         self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
#         self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text') 
#         self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')
        
#     def check_visible(self, title: str, description: str):
#         expect(self.icon).to_be_visible()
        
#         expect(self.title).to_be_visible()
#         expect(self.title).to_have_text(title)
        
#         expect(self.description).to_be_visible()
#         expect(self.description).to_have_text(description)

from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Empty icon')
        self.title = Text(page, f'{identifier}-empty-view-title-text', 'Empty title')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Empty description')

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)