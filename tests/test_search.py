from config import TestData
from pages.locators import AuthLocators
from pages.auth_page import AuthPage
from tests.test_base import BaseTest


class TestSearch(BaseTest):
   def test_search_by_text(self):
      """Проверяем, что поле поиска осуществляет поиск по введенному слову"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.text_search_1)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # записываем url текущей страницы
      search_url = self.authPage.get_url()
      # проверяем, что в url  содержится 'search'
      assert TestData.text_search_url in search_url
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.text_search_1)
      # проверяем, что в результате поиска нашлась хотябы одна книга
      SEARCH_BOOKS = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      assert len(SEARCH_BOOKS) > 0


   def test_double_search(self):
      """Проверяем возможность удаления параметра предыдущего поиска и ввода новых параметров"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.text_search_1)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.text_search_1)
      # проверяем, что в результате поиска нашлась хотябы одна книга
      SEARCH_BOOKS_1 = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      assert len(SEARCH_BOOKS_1) > 0
      # очищаем поле ввода и вводим новый параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.text_search_2)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.text_search_2)
      # проверяем, что в результате поиска нашлась хотябы одна книга
      SEARCH_BOOKS_2 = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      assert len(SEARCH_BOOKS_2) > 0


   def test_empty_search_field(self):
      """Проверяем отсутствие возможности поиска по пустому полю"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и нажимаем иконку "поиск"
      self.authPage.clear_field(AuthLocators.AUTH_SEARCH_FIELD)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # записываем url текущей страницы и проверяем, что мы остались на стартовой стртанице и не перешли на страницу поиска
      search_url = self.authPage.get_url()
      assert search_url == TestData.START_URL



   def test_search_translates_lati_into_rus(self):
      """Проверяем, что поле поиска русские слова, написанные на английской раскладке клавиатуры,
      переводит на русский язык в заголовке запроса"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_latin)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.author_last_name_rus)

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_latin)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT,
                                                       TestData.title_book_rus)

   def test_search_255_symbols(self):
      """Проверяем возможность ввести в поле поиска 256 символов и перейти на страницу с результатами поиска"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.symbol_256)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # записываем url текущей страницы
      search_url = self.authPage.get_url()
      # проверяем, что в url  содержится 'search'
      assert TestData.text_search_url in search_url


   def test_search_special_symbols(self):
      """Проверяем возможность ввести в поле поиска специальные символы и перейти на страницу с результатами поиска"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.special_symbol)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # записываем url текущей страницы
      search_url = self.authPage.get_url()
      # проверяем, что в url  содержится 'search'
      assert TestData.text_search_url in search_url


   def test_search_by_author_rus(self):
      """Проверяем возможность поиска книги "Три мушкетера" А.Дюма по фамилии автора на русском языке"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_rus)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.author_last_name_rus)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.author_last_name_rus)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_author_eng(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по фамилии автора на английском языке"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_eng)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.author_last_name_eng)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.author_last_name_eng)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_author_latin(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по фамилии автора, написанной русским текстом
       на английской раскладке клавиатуры"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_latin)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.author_last_name_rus)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.author_last_name_latin)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_author_rus_initials_1(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по фамилии автора с инициалами"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_rus_initials_1)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.author_rus_initials_1)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # проверяем наличие кнопки и нажимаем на кнопку "Следующая"
            assert self.authPage.elements_find(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE), 'Проверены все {} страницы, по параметру "{}" искомая книга не найдена'.format(i, TestData.author_rus_initials_1)
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.author_rus_initials_1)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_author_rus_initials_2(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по фамилии автора с инициалами через пробел"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_rus_initials_2)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.author_rus_initials_2)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # проверяем наличие кнопки и нажимаем на кнопку "Следующая"
            assert self.authPage.elements_find(
               AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE), 'Проверены все {} страницы, по параметру "{}" искомая книга не найдена'.format(
               i, TestData.author_rus_initials_2)
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.author_rus_initials_2)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()



   def test_search_by_title_book_rus(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по названию книги на русском языке"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_rus)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_rus)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_rus)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_title_book_eng(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по названию книги на английском языке"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_eng)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_eng)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS_1).text)

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      i = 1
      while i < total_pages_search_books:
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_eng)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()



   def test_search_by_title_book_latin(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по названию книги, аписанной русским текстом
       на английской раскладке клавиатуры"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_latin)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_rus)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_latin)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()



   def test_search_by_title_book_first_part(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по первому слову названия книги"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_first_part)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_first_part)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_first_part)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()



   def test_search_by_title_book_end_part(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по последнему слову в названии книги"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_end_part)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_end_part)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_end_part)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_title_book_topic(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по теме книги"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_topic)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_topic)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_topic)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_by_title_book_figure(self):
      """Тест проверяет возможность поиска книги "Три мушкетера" А.Дюма по фамилии автора с инициалами"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()

      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_figure)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # проверяем, что на странице в заголовке результата поиска содержатся параметры поиска
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_TITLE_SEARCH_RESULT, TestData.title_book_figure)

      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))

      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))

      # проверяем наличие искомой книги постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем наличие искомой книги на странице и видимость ее на странице
      assert self.authPage.elements_find(
         AuthLocators.AUTH_BOOK_TRI_MUSKETEERS), 'Поиск по параметру "{}" не находит искомую книгу'.format(
         TestData.title_book_figure)
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()


   def test_search_page_book(self):
      """Проверяем возможность попасть на страницу книги через поиск"""
      self.authPage = AuthPage(self.driver)
      # # принимает cookies и закрывает окно
      # self.authPage.accept_cookies_btn()
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_rus)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # записываем в переменную все найденные книги на странице
      search_books = self.authPage.all_elements_are_presents(AuthLocators.AUTH_SEARCH_BOOKS)
      # записываем в переменную общее количество найденных книг по параметру поиска
      TOTAL_NUMBER_SEARCH_BOOKS = int(
         (self.authPage.element_are_present(AuthLocators.AUTH_TOTAL_NUMBER_SEARCH_BOOKS).text).replace(" ", ""))
      # высчитываем количество страниц с результатами поиска
      if int(TOTAL_NUMBER_SEARCH_BOOKS) % len(search_books) > 0:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books)) + 1
      else:
         total_pages_search_books = int(int(TOTAL_NUMBER_SEARCH_BOOKS) / len(search_books))
      # ищем искомую книгу постранично
      for i in range(total_pages_search_books):
         if self.authPage.elements_find_true(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS):
            break
         else:
            # кликаем на кнопку "Следующая"
            self.authPage.click_element(AuthLocators.AUTH_SEARCH_BTN_NEXT_PAGE)

      # проверяем видимость книги на странице, нажимаем на неё
      BOOK_TRI_MUSKETEERS = self.authPage.element_are_present(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)
      assert BOOK_TRI_MUSKETEERS.is_displayed()
      self.authPage.hover_cursor_click(AuthLocators.AUTH_BOOK_TRI_MUSKETEERS)

      # проверяем, что попали на страницу книги: в url страницы есть id искомой книги
      search_book_url = self.authPage.get_url()
      assert TestData.ID_TRI_MUSKEETERS in search_book_url


   def test_search_pop_up_you_were_looking(self):
      """Проверяем наличие у поля поиска всплывающего окна с истрией поиска,
      проверяет, что поле поиска запоминает вводимые параметры поиска"""
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_rus)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # очищаем поле ввода и вводим новый параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_id)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)

      # нажимаем на логотип и возвращаемся на стартовую страницу
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      # проверяем, что всплывающее окно не видно на экране
      assert self.authPage.element_invisibility(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)

      # нажимаем на поле поиска
      self.authPage.hover_cursor_click(AuthLocators.AUTH_SEARCH_FIELD)

      # проверяем присутствие всплывающего окна на странице и видимость его на экране
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)
      POP_UP_SEARCH_FIELD_HISTORY = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)
      assert POP_UP_SEARCH_FIELD_HISTORY.is_displayed()

      # записываем в переменную весь текст из всплывающего окна
      POP_UP_SEARCH_FIELD_HISTORY_TEXT = self.authPage.get_element_text(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)

      # проверяем, что в тексте всплывающего окна содержатся параметры двух запросов
      assert TestData.author_last_name_rus in POP_UP_SEARCH_FIELD_HISTORY_TEXT
      assert TestData.title_book_id in POP_UP_SEARCH_FIELD_HISTORY_TEXT



   def test_search_pop_up_what_looking(self):
      """Проверяем появление всплывающего окна после ввода текста в поле поиска"""
      self.authPage = AuthPage(self.driver)
      # проверяем, что всплывающее окно не видно на экране
      assert self.authPage.element_invisibility(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_WHAT_THEY_LOOKING)

      # очищаем поле ввода и вводим параметр поиска
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_rus)
      # нажимаем на поле поиска
      self.authPage.hover_cursor_click(AuthLocators.AUTH_SEARCH_FIELD)

      # проверяем, что всплывающее окно присутствует на странице и видно на экране
      POP_UP_SEARCH_FIELD_WHAT_THEY_LOOKING = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_WHAT_THEY_LOOKING)
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_WHAT_THEY_LOOKING)
      assert POP_UP_SEARCH_FIELD_WHAT_THEY_LOOKING.is_displayed()


   def test_search_pop_up_clear_query_history(self):
      """Проверяем возможность очистки истории запросов кнопкой "Очистить всю историю запросов" """
      self.authPage = AuthPage(self.driver)
      # очищаем поле ввода и вводим параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.author_last_name_rus)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # очищаем поле ввода и вводим новый параметр поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_id)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # нажимаем на логотип и возвращаемся на стартовую страницу
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      # нажимаем на поле поиска
      self.authPage.hover_cursor_click(AuthLocators.AUTH_SEARCH_FIELD)

      # записываем в переменную весь текст из всплывающего окна
      POP_UP_SEARCH_FIELD_HISTORY_TEXT = self.authPage.get_element_text(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)
      # проверяем, что в тексте всплывающего окна содержатся параметры двух запросов
      assert TestData.author_last_name_rus in POP_UP_SEARCH_FIELD_HISTORY_TEXT
      assert TestData.title_book_id in POP_UP_SEARCH_FIELD_HISTORY_TEXT

      # нажимаем кнопку "Очистить всю историю запросов" на всплывающем окне
      self.authPage.hover_cursor_click(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_CLEAR_HISTORY)

      # проверяем, что история очистилась; нажимаем на логотип и обновляем страницу
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      # нажимаем на поле поиска
      self.authPage.hover_cursor_click(AuthLocators.AUTH_SEARCH_FIELD)
      # проверяем, что всплывающее окно не появляется на экране
      assert self.authPage.element_invisibility(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)

      # дополнительная проверка, что история очистилась
      # очищаем поле ввода и вводим параметр нового поиска, нажимаем иконку "поиск"
      self.authPage.click_clear_send_text(AuthLocators.AUTH_SEARCH_FIELD, TestData.title_book_rus)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_ICON_SEARCH_FIELD)
      # нажимаем на логотип и возвращаемся на стартовую страницу
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      # нажимаем на поле поиска
      self.authPage.hover_cursor_click(AuthLocators.AUTH_SEARCH_FIELD)

      # записываем в переменную весь текст из всплывающего окна
      POP_UP_SEARCH_FIELD_HISTORY_TEXT_NEW = self.authPage.get_element_text(AuthLocators.AUTH_POP_UP_SEARCH_FIELD_3)
      # проверяем, что в тексте всплывающего окна содержится параметр нового запроса
      assert TestData.title_book_rus in POP_UP_SEARCH_FIELD_HISTORY_TEXT_NEW
      # проверяем, что в тексте всплывающего окна НЕ содержатся параметры старых запросов
      assert TestData.author_last_name_rus not in POP_UP_SEARCH_FIELD_HISTORY_TEXT_NEW
      assert TestData.title_book_id not in POP_UP_SEARCH_FIELD_HISTORY_TEXT_NEW
