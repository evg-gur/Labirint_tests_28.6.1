from config import TestData
from pages.locators import AuthLocators
from pages.auth_page import AuthPage
from tests.test_base import BaseTest


class TestAccess(BaseTest):
   def test_access_button_activity_min_numbers(self):
      """Проверяем, что кнопка "Войти" становится активной после ввода 10-ти цифр"""
      self.authPage = AuthPage(self.driver)
      # нажимаем на кнопку "Мой Лаб"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость формы регистрации на экране
      assert self.authPage.element_visibility(AuthLocators.AUTH_AUTHORIZATION_WINDOW)
      # проверяем, что кнопка "Войти" в данный момент не включена (is_enabled() == False)
      BTN_LOGIN = self.authPage.element_find(AuthLocators.AUTH_ACCESS_BTN_LOGIN)
      assert  BTN_LOGIN.is_enabled() == False
      # Очищаем поле ввода и проверяем, что кнопка "Войти" не включена
      self.authPage.clear_field(AuthLocators.AUTH_ACCESS_INPUT_FIELD)
      assert  BTN_LOGIN.is_enabled() == False
      i = 0
      while BTN_LOGIN.is_enabled() == False:
         # в поле вводим по одной цифре 1 (TestData.number = 1)
         self.authPage.send_text_1(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.number)
         i += 1

      # проверяем, что кнопка "Войти" стала активной
      assert BTN_LOGIN.is_enabled
      # проверяем, что потребовалось ввести 10 цифр (т.е. минимальнодопустимое количество)
      assert i == TestData.min_number


   def test_access_button_activity_min_letters_eng(self):
      """Проверяем, что кнопка "Войти" становится активной после ввода 12-ти букв"""
      self.authPage = AuthPage(self.driver)
      # нажимаем на кнопку "Мой Лаб"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость формы регистрации на экране
      assert self.authPage.element_visibility(AuthLocators.AUTH_AUTHORIZATION_WINDOW)
      # проверяем, что кнопка "Войти" в данный момент не включена (is_enabled() == False)
      BTN_LOGIN = self.authPage.element_find(AuthLocators.AUTH_ACCESS_BTN_LOGIN)
      assert  BTN_LOGIN.is_enabled() == False
      # Очищаем поле ввода и проверяем, что кнопка "Войти" не включена
      self.authPage.clear_field(AuthLocators.AUTH_ACCESS_INPUT_FIELD)
      assert  BTN_LOGIN.is_enabled() == False
      i = 0
      while BTN_LOGIN.is_enabled() == False:
         # в поле вводим по одной цифре 1 (TestData.number = 1)
         self.authPage.send_text_1(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.letter_eng)
         i += 1

      # проверяем, что кнопка "Войти" стала активной
      assert BTN_LOGIN.is_enabled
      # проверяем, что потребовалось ввести 10 цифр (т.е. минимальнодопустимое количество)
      assert i == TestData.min_letters


   def test_access_button_activity_min_letters_rus(self):
      """Проверяем, что кнопка "Войти" становится активной после ввода 12-ти букв"""
      self.authPage = AuthPage(self.driver)
      # нажимаем на кнопку "Мой Лаб"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость формы регистрации на экране
      assert self.authPage.element_visibility(AuthLocators.AUTH_AUTHORIZATION_WINDOW)
      # проверяем, что кнопка "Войти" в данный момент не включена (is_enabled() == False)
      BTN_LOGIN = self.authPage.element_find(AuthLocators.AUTH_ACCESS_BTN_LOGIN)
      assert  BTN_LOGIN.is_enabled() == False
      # Очищаем поле ввода и проверяем, что кнопка "Войти" не включена
      self.authPage.clear_field(AuthLocators.AUTH_ACCESS_INPUT_FIELD)
      assert  BTN_LOGIN.is_enabled() == False
      i = 0
      while BTN_LOGIN.is_enabled() == False:
         # в поле вводим по одной цифре 1 (TestData.number = 1)
         self.authPage.send_text_1(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.letter_rus)
         i += 1

      # проверяем, что кнопка "Войти" стала активной
      assert BTN_LOGIN.is_enabled
      # проверяем, что потребовалось ввести 10 цифр (т.е. минимальнодопустимое количество)
      assert i == TestData.min_letters


   def test_access_length_input_string(self):
      """ТПроверяем, что поле ввода не принимает более 50 цифр"""
      self.authPage = AuthPage(self.driver)
      # проверяем присутствие элемента на странице
      assert self.authPage.element_are_present(AuthLocators.AUTH_ACCESS_INPUT_FIELD)
      # проверяем, что строка ввода имеет атрибут максимальной длины строки
      max_long_input_string = int(self.authPage.get_attribute_value(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.attribut_input_string))
      assert max_long_input_string
      assert max_long_input_string > 0


   def test_access_input_email_correct(self):
      """Проверяем, что поле ввода принимает корректный email и кнопка "Войти" становится активной"""
      self.authPage = AuthPage(self.driver)
      # нажимаем на кнопку "Мой Лаб"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость формы регистрации на экране
      assert self.authPage.element_visibility(AuthLocators.AUTH_AUTHORIZATION_WINDOW)

      # проверяем, что кнопка "Войти" в данный момент не включена (is_enabled() == False)
      BTN_LOGIN = self.authPage.element_find(AuthLocators.AUTH_ACCESS_BTN_LOGIN)
      assert  BTN_LOGIN.is_enabled() == False
      # Очищаем поле ввода
      self.authPage.clear_field(AuthLocators.AUTH_ACCESS_INPUT_FIELD)

      # в поле вводим email
      self.authPage.send_text_1(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.email)

      # проверяем, что кнопка "Войти" стала активной
      assert BTN_LOGIN.is_enabled
      # получаем текст комментария под полем ввода и сравниваем его с текстом, который подтверждает корректность данных
      ACCESS_BTN_LOGIN_COMMENT = self.authPage.get_element_text(AuthLocators.AUTH_ACCESS_INPUT_FIELD_COMMENT)
      assert ACCESS_BTN_LOGIN_COMMENT == TestData.comment_login


   def test_access_input_email_incorrect(self):
      """Проверяем, что поле ввода принимает некорректный email и кнопка "Войти" становится активной"""
      self.authPage = AuthPage(self.driver)
      # нажимаем на кнопку "Мой Лаб"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость формы регистрации на экране
      assert self.authPage.element_visibility(AuthLocators.AUTH_AUTHORIZATION_WINDOW)

      # проверяем, что кнопка "Войти" в данный момент не включена (is_enabled() == False)
      BTN_LOGIN = self.authPage.element_find(AuthLocators.AUTH_ACCESS_BTN_LOGIN)
      assert  BTN_LOGIN.is_enabled() == False
      # Очищаем поле ввода
      self.authPage.clear_field(AuthLocators.AUTH_ACCESS_INPUT_FIELD)

      # в поле вводим email
      self.authPage.send_text_1(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.email_incorrect)

      # проверяем, что кнопка "Войти" стала активной
      assert BTN_LOGIN.is_enabled
      # получаем текст комментария под полем ввода и сравниваем его с текстом, который подтверждает корректность данных
      ACCESS_BTN_LOGIN_COMMENT = self.authPage.get_element_text(AuthLocators.AUTH_ACCESS_INPUT_FIELD_COMMENT)
      assert ACCESS_BTN_LOGIN_COMMENT == TestData.comment_login


   def test_access_input_special_symbol(self):
      """Проверяем, что поле ввода не принимает специальные символы"""
      self.authPage = AuthPage(self.driver)
      # нажимаем на кнопку "Мой Лаб"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость формы регистрации на экране
      assert self.authPage.element_visibility(AuthLocators.AUTH_AUTHORIZATION_WINDOW)
      # Очищаем поле ввода
      self.authPage.clear_field(AuthLocators.AUTH_ACCESS_INPUT_FIELD)

      # в поле вводим специальные символы
      self.authPage.send_text_1(AuthLocators.AUTH_ACCESS_INPUT_FIELD, TestData.special_symbol)
      # проверяем, что под строкой появляется текст с предупреждением об ошибке
      # получаем текст комментария
      ACCESS_INPUT_FIELD_COMMENT_ERROR = self.authPage.get_element_text(AuthLocators.AUTH_ACCESS_INPUT_FIELD_COMMENT)
      # проверяем, что в тексте содержится фраза "Нельзя использовать символ"
      assert TestData.comment_symbol_cannot_used in ACCESS_INPUT_FIELD_COMMENT_ERROR









