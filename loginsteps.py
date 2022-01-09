import time

from behave import given, when, then

from BrainBucket.pages.login_page import LoginPage
from time import sleep
from BrainBucket.pages.profile_page import ProfilePage
from BrainBucket.utils.config_reader import ConfigReader
from BrainBucket.webelements.browser import Browser


# URL = "https://techskillacademy.net/brainbucket/index.php?route=account/login"
# configs = ConfigReader("BrainBucketTests/BDDBehave/logintests/steps/config.ini")


# @given("user launch login page")
# def launch_login_page(context):
# browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
# context.browser = browser


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page
    time.sleep(3)


@when('user types "{value}" in "{field}"')
def type_value_in_field(context, value, field):
    login_page = LoginPage(context.browser)
    context.login_page = login_page

    if field == 'email':
        login_page.enter_email(value)
        time.sleep(2)

    elif field == 'password':
        login_page.enter_password(value)
        time.sleep(2)

@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()
    time.sleep(3)


@then("warning is shown that no match email or password")
def verify_user_login_view(context):
    login_page = context.login_page
    print("PULL TEXT IS !!!!!!", login_page.get_login_warning())
    assert login_page.get_login_warning() == "Warning: No match for E-Mail Address and/or Password."



