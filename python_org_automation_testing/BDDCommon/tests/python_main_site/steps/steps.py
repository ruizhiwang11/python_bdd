from BDDCommon.CommonSteps.websteps_common import *

@then('the {nav_bar} bar should be visible')
def verify_nav_bar_visible(context, nav_bar):

    expected_bars = ["main navigation", 'top navigation', 'options']
    print(nav_bar)
    if nav_bar not in expected_bars:

        raise RuntimeError("The passed in nav_bar type is not the one expected")
    if nav_bar == 'main navigation':
        locator = 'html/div/div[5]'
        bar = context.driver.find_element_by_xpath(locator)
        if not bar.is_visible():
            raise RuntimeError("run time error")
    elif nav_bar == 'top navigation':
        pass
    else:
        pass
