from behave import given, when, then
import logging as logger

@given("I am the main directory")
def in_main_dir(context):
    pass

@then("I should also be in the main directory")
def also_in_main_dir(context):
    print("111111")
    print("1111")
    logger.info("I am info")
    logger.debug("I am debug")
    assert 1 == 2
