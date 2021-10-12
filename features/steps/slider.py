from behave import when,then
import time

from numpy.testing import assert_equal
from selenium import webdriver
import os
from selenium.webdriver import ActionChains



@when(u'he slide the cursor to the left')
def step_impl(context):
    context.dd.slid()


@then(u'he got for a value of 100')
def step_impl(context):

    mon_msg = context.dd.affich_slid()
    assert_equal(mon_msg.text,"100")




