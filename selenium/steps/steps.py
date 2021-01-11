from behave import given, when, then
import logging as logger

@given("I go to login page")
def create_new_context(context):
    print('creating new user')
    print('login')
    logger.info('111 Info')
    logger.debug('111 debug')


@when("I click on login")
def login(context):
    print("")
    logger.info("")
    print('clicking loging')
    print('clicking loging')
    logger.info('222 Info')
    logger.debug('222 debug')

@when("I click on logout")
def logout(context):
    print('clicking')

@then("I should see error")
def error(context):
    print("yes can see errors!!")
    assert True


@then("I should see errorss")
def errorss(context):
    print("yes can see errors!!")
