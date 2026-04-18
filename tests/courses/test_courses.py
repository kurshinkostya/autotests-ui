import allure
import pytest

from playwright.sync_api import Page

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
        )

        create_course_page.toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.form.check_visible(
            title="", 
            max_score="0", 
            min_score="0", 
            description="", 
            estimated_time=""
        )

        create_course_page.exercises_toolbar.check_visible()

        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.form.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright course description",
            estimated_time="2 weeks"
        )

        create_course_page.toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, 
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
    
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
        )

        courses_list_page.navbar.check_visible("username")

        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()
    
    @allure.title("Edit course")
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_data = {
            "title": "Playwright",
            "estimated_time": "2 weeks",
            "description": "Playwright course description",
            "max_score": "100",
            "min_score": "10"
        }

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.form.fill(**create_data)

        create_course_page.toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible(
            index=0,
            title=create_data["title"],
            max_score=create_data["max_score"],
            min_score=create_data["min_score"],
            estimated_time=create_data["estimated_time"]
        )

        courses_list_page.course_view.menu.click_edit(index=0)

        updated_data = {
            "title": "Allure",
            "estimated_time": "3 weeks",
            "description": "Alluree course description",
            "max_score": "200",
            "min_score": "20"
        }

        create_course_page.form.fill(**updated_data)

        create_course_page.toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title=updated_data["title"],
            max_score=updated_data["max_score"],
            min_score=updated_data["min_score"],
            estimated_time=updated_data["estimated_time"]
        )
    