from enum import Enum


class AllureStory(str, Enum):
    COURSES = 'COURSES'
    DASHBOARD = 'DASHBOARD'
    REGISTRATION = 'REGISTRATION'
    AUTHENTICATION = 'AUTHENTICATION'