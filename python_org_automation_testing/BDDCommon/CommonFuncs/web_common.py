from selenium import webdriver


def go_to(url: object, browser_type: object = None) -> object:
    """
    :param url: the url to navigate to
    :param browser_type: the type of browser to start
    :return: driver: webdriver instance
    """

    if not browser_type:
        driver = webdriver.Firefox()
    elif browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"The browser type {browser_type} is unsupported")
    driver.get(url)
    return driver


def assert_page_title(context, expected_title):
    actual_title = context.driver.title
    print(f"The actual title is: {actual_title}")
    print(f"The expected title is {expected_title}")

    assert expected_title == actual_title, f"The title is not as expected. \
                                            Expected: {expected_title}, Actual: {actual_title}"


def assert_current_url(context, expected_url: str):

    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = "https://".join(f"{expected_url}/")
    assert current_url == expected_url, f"The current url is not as expected. \
                                        Expected: {expected_url}, Actual: {current_url}"


def assert_text_visible(text):
    pass


def assert_element_visible(element):
    pass
