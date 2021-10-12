import os

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from pages.drag_drop import dragdrop


def before_scenario(context,scenario):

    dir = os.getcwd()

    option = webdriver.ChromeOptions()
    #option.add_argument("--start_maximized")
    option.add_argument("headless")
    context.browser = webdriver.Chrome(executable_path=dir + "\drivers\chromedriver.exe",chrome_options=option)



    context.browser.maximize_window()

    #création d'une nouvelle instance
    context.dd = dragdrop(context.browser)


def after_scenario(context,scenario):
    context.browser.close()


def after_step(context, step):
    if step.status == "failed":
        context.browser.save_screenshot('c://b/screenshot.png')
        attach(
            context.browser.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG)

