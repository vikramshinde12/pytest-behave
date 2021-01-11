from behave import given, when, then
import pdb


@given("I create {gender} user")
def user(context, gender):
    context.user = gender
    print("")

    print(f'created {gender} user ***')


@when("I login with the user")
def login(context):
    print('login ***')
    assert True


@then("the page color should {color}")
def page(context, color):
    user = context.user
    print(f"{user} can see {color} color ****")