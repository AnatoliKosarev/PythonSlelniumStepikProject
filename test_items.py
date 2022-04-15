import time

from selenium.webdriver.common.by import By


def test_add_to_basket_btn_shown(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(10)
    add_to_basket_btn = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')

    assert len(add_to_basket_btn) == 1, 'Add to basket button is missing on the page'
