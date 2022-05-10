from behave import given, then, when


@given("I have a new {item} in my cart")
def i_have_ittem(context, item):
    print(f"The item is: {item}")


@when('I click on "{button_to_click}"')
def click_button(context, button_to_click):
    print(f"I'm clicking hte button: {button_to_click}")


@then('I should see "{txt}"')
def i_should_see_text(context, txt):
    print(txt)
    if txt not in ["success", "error"]:
        raise Exception("Unexpected text passed in")

    print(f"Checking if I see the {txt} text")
    print(f"PASS, I see the {txt} text")
