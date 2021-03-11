from selenium import webdriver
import time
import unittest


class TestRegSite(unittest.TestCase):

    def test_reg_site_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(3)

        input1 = browser.find_element_by_css_selector('.first_block .first_class input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second_class input')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third_class input')
        input3.send_keys("email@email.em")

        # Проверяем заполнение полей
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # Находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        # Записываем в переменную welcome_text из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')

    def test_reg_site_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block .first_class input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second_class input')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third_class input')
        input3.send_keys("email@email.em")

        # Проверяем заполнение полей
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # Находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        # Записываем в переменную welcome_text из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')


if __name__ == '__main__':
    unittest.main()