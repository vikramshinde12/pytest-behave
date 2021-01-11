from behave import given, when, then


@given("I have a new {item} in my cart")
def i_have_item_in_cart(context, item):
    print("")
    context.order_number = 112233
    print(f"The item is {item}")


@when("I click on {button} button")
def press(context, button):
    print(f"pressing {button}")

@then("It gives me error")
def error(ccoo):
    print(f"finishing the order number {ccoo.order_number}")