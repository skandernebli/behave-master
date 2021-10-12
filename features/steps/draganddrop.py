from behave import given,when,then
from selenium import webdriver
from selenium.webdriver import ActionChains
from numpy.testing import assert_equal


@given(u'the user navigate to the drag and drop URL')
def step_impl(context):
    #context.browser.get("https://qavbox.github.io/demo/dragndrop/")
    context.dd.setup("https://qavbox.github.io/demo/dragndrop/")


@when(u'he drag and drop the grey square in the blue square')
def step_impl(context):
    context.dd.drag()


@then(u'he sees a message "Dropped!"')
def step_impl(context):
    context.dd.affi()
    msg = context.dd.affi()
    assert_equal(msg.text,"Dropped!")
