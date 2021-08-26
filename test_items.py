import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_page_has_basket_button(browser):
    browser.get(link)
    # time.sleep(30) слишком долго ждать, но если хочется... 
    time.sleep(10)
    #time.sleep(30)
    basket_button = browser.find_elements_by_class_name('btn-add-to-basket')
    assert basket_button != [], 'Кнопка "Добавить в корзину не найдена"'
    
    
    
