from config import TestData
from pages.locators import AuthLocators
from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.START_URL)


    def all_elements_are_presents(self, locator):
        """метод ожидает, что все элементы с данным локтором присутствуют на странице"""
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def element_are_present(self, locator):
        """метод ожидает, что элемент с данным локтором присутствует на странице"""
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element


    def element_find(self, locator):
        """Метод ищет элемент по локатору"""
        element = self.driver.find_element(*locator)
        return element


    def elements_find(self, locator):
        """Метод ищет элементы по локатору"""
        elements = self.driver.find_elements(*locator)
        return elements

    def elements_find_true(self, locator) -> bool:
        """Метод возвращает True, если элемен есть на странице"""
        elements = self.driver.find_elements(*locator)
        return bool(elements)

    def missing_element(self, locator):
        """Метод ожидает отсутствия элемента на странице"""
        element = WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))
        return element

    def missing_element_true(self, locator) -> bool:
        """Метод возвращает True, если элемен отсутствует на странице"""
        element = WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))
        return bool(element)


    def element_visibility(self, locator):
        """метод ожидает, что элемент с данным локтором виден на экране"""
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def element_invisibility(self, locator):
        """метод ожидает, что элемент с данным локтором не виден на экране"""
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.invisibility_of_element_located(locator))
        return element


    def element_visibility_true(self, element_page) -> bool:
        """Метод определяет True: элемнт виден на экране"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element_page))
        return bool(element)

    def element_invisibility_true(self, element_page) -> bool:
        """Метод определяет True: элемнт не виден на экране"""
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of(element_page))
        return bool(element)

    def element_present_true(self, locator) -> bool:
        """Метод определяет True: элемент присутствует на странице"""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return bool(element)


    def text_are_present_in_element(self, locator, text):
        """метод ожидает присутствие текста внутри элемента"""
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.text_to_be_present_in_element(locator, text))
        return element
        # assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "PetFriends"))

    def scroll_to_element(self, element):
        """метод скроллит страницу до указанного элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def accept_cookies_btn(self):
        """метод находит всплывающее окно с предупреждением о cookies и нажимает кнопку Принять"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_ACCEPT_COOKIES_BTN)).click()

    def hover_cursor(self, locator):
        """Метод наводит курсор на элемент, найденный по локатору"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def hover_cursor_click(self, locator):
        """Метод наводит курсор на элемент, найденный по локатору и нажимает на него"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click(element).perform()

    def click_element(self, locator):
        """Метод нажимает на элемент, найденный по локатору"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.click(element).perform()

    def get_element_text(self, locator):
        """Метод возвращает текст елемента по указанному локатору"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text


    def get_url(self):
        """Метод возвращает полный URL страницы"""
        page_url = self.driver.current_url
        return page_url

    def click_clear_send_text(self, locator, text):
        """Метод кликает в поле, очищает его и вводит текст"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()
        element.send_keys(text)

    def click_clear_field(self, locator):
        """Метод кликает в поле и очищает его от текста"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()

    def clear_field(self, locator):
        """Метод очищает поле от текста"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()


    def send_text(self, locator, text):
        """Метод вводит текст"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def send_text_1(self, locator, text):
        """Метод вводит текст"""
        element = self.driver.find_element(*locator)
        return element.send_keys(text)


    def get_attribute_value(self, locator, attr_name):
        """Метод возвращает значение атрибута по названию атрибута и локатору"""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        value = element.get_attribute(attr_name)
        return value

    def elementes_get_attribute_value(self, locator, attribut):
        """Метод возвращает список значений атрибута елементов, найденных по локатору"""
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        list_attr_name = []
        for i in range(len(elements)):
            value = elements[i].get_attribute(attribut)
            list_attr_name.append(value)
        return list_attr_name
