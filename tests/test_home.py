from config import TestData
from pages.locators import AuthLocators
from pages.auth_page import AuthPage
from tests.test_base import BaseTest


class TestStartPage(BaseTest):
   def test_start_page_product(self):
      """Проверяем наличие на главной странице карточек с товаром и наличие у товара параметров: фото,
      кнопки "Добаить в избранное" и "В корзину", название книги, цена"""
      self.authPage = AuthPage(self.driver)
      # 1) Проверяем что на странице присутствуют product-книги
      START_PAGE_BOOKS = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS)
      assert len(START_PAGE_BOOKS) > 0
      # 2) Ищем и проверяем что на главной странице product-книги имеют фото, имя, цену, "избранное", "в корзину"
      START_PAGE_BOOKS_IMG = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS_IMG)
      START_PAGE_BOOKS_NAME = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS_NAME)
      START_PAGE_BOOKS_PRICE = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS_PRICE)
      START_PAGE_BOOKS_BTN_FAVOURITES = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS_FAVOURITES)
      START_PAGE_BOOKS_BTN_CART = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS_BTN_CART)
      for i in range(len(START_PAGE_BOOKS)):
         assert START_PAGE_BOOKS_IMG[i].get_attribute(TestData.IMG_attribute) != ''
         assert START_PAGE_BOOKS_NAME[i].text != '', "У книги № {} нет имени".format(i+1)
         assert START_PAGE_BOOKS_PRICE[i].text != '', "У книги № {} нет цены".format(i+1)
         assert START_PAGE_BOOKS_BTN_FAVOURITES[i].is_displayed(), "Книгу № {} нельзя добавить в избранное".format(i+1)
         assert START_PAGE_BOOKS_BTN_CART[i].text == TestData.TEXT_BTN_CART or TestData.TEXT_BTN_CART_1, "Книгу № {} нельзя заказать".format(i+1)


   def test_go_to_page_putorder(self):
      """Проверяем, что в шапке сайта кнопка "Отложено" переводит на страницу START_URL + 'cabinet/putorder/'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_PUTORDER = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)
      assert HEADER_BUTTON_PUTORDER.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)
      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      PUTORDER_URL = self.authPage.get_url()
      assert PUTORDER_URL == TestData.PUTORDER_URL


   def test_go_to_page_cart(self):
      """Проверяем, что в шапке сайта кнопка "Корзина" переводит на страницу START_URL + '.../'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_CART = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CART)
      assert HEADER_BUTTON_CART.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_CART)
      # открывается страница "Корзина", получаем URL новой страницы и сравниваем с данными из config.py
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL


   def test_go_to_page_call(self):
      """Проверяем, что в шапке сайта кнопка "Позвонить" переводит на страницу START_URL + '.../'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_CALL = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CALL)
      assert HEADER_BUTTON_CALL.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_CALL)
      # открывается страница "Контакты", получаем URL новой страницы и сравниваем с данными из config.py
      CALL_URL = self.authPage.get_url()
      assert CALL_URL == TestData.CALL_URL


   def test_go_to_page_my_labirint_without_authorization(self):
      """Проверяем, что в шапке сайта кнопка "Мой лабиринт" открывает форму регистрации 'Полный доступ к Лабиринту'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_MY_LABIRINT = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      assert HEADER_BUTTON_MY_LABIRINT.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      # проверяем видимость на экране формы регистрации "Полный доступ к Лабиринту"
      REGISTRATION_FORM_MY_LABIRINT = self.authPage.element_are_present(AuthLocators.AUTH_REGISTRATION_FORM_MY_LABIRINT)
      assert REGISTRATION_FORM_MY_LABIRINT.is_displayed(), "Элемент не виден на дисплее"
      # проверяем присутствие в форме текста "Полный доступ к Лабиринту"
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_REGISTRATION_FORM_MY_LABIRINT, "Полный доступ к Лабиринту")


   def test_go_to_page_messages_without_authorization(self):
      """Проверяем, что в шапке сайта кнопка "Сообщения" открывает форму регистрации 'Полный доступ к Лабиринту'"""
      self.authPage = AuthPage(self.driver)
      HEADER_BUTTON_MESSAGES = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_MESSAGES)
      assert HEADER_BUTTON_MESSAGES.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_MESSAGES)
      # проверяем видимость на экране формы регистрации "Мой лаюиринт"
      REGISTRATION_FORM_MY_LABIRINT = self.authPage.element_are_present(
            AuthLocators.AUTH_REGISTRATION_FORM_MY_LABIRINT)
      assert REGISTRATION_FORM_MY_LABIRINT.is_displayed(), "Элемент не виден на дисплее"
      # проверяем присутствие в форме текста "Полный доступ к Лабиринту"
      assert self.authPage.text_are_present_in_element(AuthLocators.AUTH_REGISTRATION_FORM_MY_LABIRINT,
                                                          "Полный доступ к Лабиринту")


   def test_displayed_heder_messages(self):
      """Проверяем наличие кнопки и иконки "Сообщения" на странице, видимость элемента на экране"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_MESSAGES), "Элемент отсутствует на странице"
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_MESSAGES), "Элемент отсутствует на странице"
      HEADER_BUTTON_MESSAGES = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_MESSAGES)
      HEADER_BUTTON_ICONS_MESSAGES = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_ICONS_MESSAGES)
      assert HEADER_BUTTON_MESSAGES.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      assert HEADER_BUTTON_ICONS_MESSAGES.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"



   def test_displayed_heder_my_labirint(self):
      """Проверяем наличие кнопки и иконки "Мой Лабиринт" на странице, видимость элемента на экране"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT), "Элемент отсутствует на странице"
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_MY_LABIRINT), "Иконка элемента отсутствует на странице"
      HEADER_BUTTON_MY_LABIRINT = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      HEADER_BUTTON_ICONS_MY_LABIRINT = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_ICONS_MY_LABIRINT)
      assert HEADER_BUTTON_MY_LABIRINT.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      assert HEADER_BUTTON_ICONS_MY_LABIRINT.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"



   def test_displayed_heder_putorder(self):
      """Проверяем наличие кнопки и иконки "Отложено" на странице, видимость элемента на экране"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_PUTORDER), "Элемент отсутствует на странице"
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_PUTORDER), "Иконка элемента отсутствует на странице"
      HEADER_BUTTON_PUTORDER = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)
      HEADER_BUTTON_ICONS_PUTORDER = self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_PUTORDER)
      assert HEADER_BUTTON_PUTORDER.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      assert HEADER_BUTTON_ICONS_PUTORDER.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"



   def test_displayed_heder_cart(self):
      """Проверяем наличие кнопки и иконки "Корзина" на странице, видимость элемента на экране"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_CART), "Элемент отсутствует на странице"
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_CART), "Иконка элемента отсутствует на странице"
      HEADER_BUTTON_CART = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CART)
      HEADER_BUTTON_ICONS_CART = self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_CART)
      assert HEADER_BUTTON_CART.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      assert HEADER_BUTTON_ICONS_CART.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"



   def test_displayed_heder_call(self):
      """Проверяем наличие кнопки и икноки "Позвонить" на странице, видимость элемента на экране"""
      self.authPage = AuthPage(self.driver)
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_CALL), "Элемент отсутствует на странице"
      assert self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_CALL), "Иконка элемента отсутствует на странице"
      HEADER_BUTTON_CALL = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CALL)
      HEADER_BUTTON_ICONS_CALL = self.authPage.element_are_present(
         AuthLocators.AUTH_HEADER_BUTTON_ICONS_CALL)
      assert HEADER_BUTTON_CALL.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      assert HEADER_BUTTON_ICONS_CALL.is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"



   def test_pop_up_window_putorder(self):
      """Проверяем, что при наведении на кнопку "Отложено" появляется всплывающее окно"""
      self.authPage = AuthPage(self.driver)
      # проверяем, что элемент присутствует на странице и не виден
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_PUTORDER)
      POP_UP_WINDOW_PUTORDER = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_PUTORDER)
      assert POP_UP_WINDOW_PUTORDER.is_displayed() == False
      # наводим курсор на кнопку "Отложено" и проверяем, что всплывающее меню видно на дисплее
      self.authPage.hover_cursor(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)
      assert POP_UP_WINDOW_PUTORDER.is_displayed()



   def test_pop_up_window_cart(self):
      """Проверяем, что при наведении на кнопку "Корзина" появляется всплывающее окно"""
      self.authPage = AuthPage(self.driver)
      # проверяем, что элемент присутствует на странице и не виден
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_CART)
      POP_UP_WINDOW_CART = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_CART)
      assert POP_UP_WINDOW_CART.is_displayed() == False
      # наводим курсор на кнопку "Корзина" и проверяем, что всплывающее меню видно на дисплее
      self.authPage.hover_cursor(AuthLocators.AUTH_HEADER_BUTTON_CART),
      assert POP_UP_WINDOW_CART.is_displayed()


   def test_pop_up_window_messages(self):
      """Проверяем, что при наведении на кнопку "Сообщения" появляется всплывающее окно"""
      self.authPage = AuthPage(self.driver)
      # проверяем, что элемент присутствует на странице и не виден
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_MESSAGES)
      POP_UP_WINDOW_MESSAGES = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_MESSAGES)
      assert POP_UP_WINDOW_MESSAGES.is_displayed() == False
      # наводим курсор на кнопку "Сообщения" и проверяем, что всплывающее меню видно на дисплее
      self.authPage.hover_cursor(AuthLocators.AUTH_HEADER_BUTTON_MESSAGES)
      assert POP_UP_WINDOW_MESSAGES.is_displayed()


   def test_pop_up_window_my_labirint(self):
      """Проверяем, что при наведении на кнопку "Мой лабиринт" появляется всплывающее окно"""
      self.authPage = AuthPage(self.driver)
      # проверяем, что элемент присутствует на странице и не виден
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_MY_LABIRINT)
      POP_UP_WINDOW_MY_LABIRINT = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_MY_LABIRINT)
      assert POP_UP_WINDOW_MY_LABIRINT.is_displayed() == False
      # наводим курсор на кнопку "Мой лабиринт" и проверяем, что всплывающее меню видно на дисплее
      self.authPage.hover_cursor(AuthLocators.AUTH_HEADER_BUTTON_MY_LABIRINT)
      assert POP_UP_WINDOW_MY_LABIRINT.is_displayed()


   def test_pop_up_window_call(self):
      """Проверяем, что при наведении на кнопку "Позвонить" появляется всплывающее окно"""
      self.authPage = AuthPage(self.driver)
      # проверяем, что элемент присутствует на странице и не виден
      assert self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_CALL)
      POP_UP_WINDOW_CALL = self.authPage.element_are_present(AuthLocators.AUTH_POP_UP_WINDOW_CALL)
      assert POP_UP_WINDOW_CALL.is_displayed() == False
      # проверяем видимость кнопки, наводим курсор на кнопку "Позвонитьт" и проверяем, что всплывающее меню видно на дисплее
      assert self.authPage.element_are_present(
            AuthLocators.AUTH_HEADER_BUTTON_CALL).is_displayed(), "Элемент не виден на дисплее при ширине окна более 1020"
      self.authPage.hover_cursor(AuthLocators.AUTH_HEADER_BUTTON_CALL)
      assert POP_UP_WINDOW_CALL.is_displayed()


   def test_logo_translates_to_start_page(self):
      """Проверяем, что нажатие на логотип в шапке сайта приводит на стартовую страницу"""
      self.authPage = AuthPage(self.driver)
      # проверяем наличие логотипа на странице и видимость логотипа на экране
      assert self.authPage.element_are_present(AuthLocators.AUTH_LOGO)
      LOGO = self.authPage.element_are_present(AuthLocators.AUTH_LOGO)
      assert LOGO.is_displayed()
      # нажимаем на логотип и проверяем, что оказались на главной странице
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      LOGO_URL = self.authPage.get_url()
      assert LOGO_URL == TestData.START_URL
      # нажимаем на кнопку "Отложить" проверяем, что оказались на странице /PUTORDER
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)
      PUTORDER_URL = self.authPage.get_url()
      assert PUTORDER_URL == TestData.PUTORDER_URL
      # нажимаем на логотип и проверяем, что оказались на главной странице
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      LOGO_URL = self.authPage.get_url()
      assert LOGO_URL == TestData.START_URL
      # нажимаем на кнопку "Корзина" проверяем, что оказались на странице /CART
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_CART)
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL
      # нажимаем на логотип и проверяем, что оказались на главной странице
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      LOGO_URL = self.authPage.get_url()
      assert LOGO_URL == TestData.START_URL
      # нажимаем на кнопку "Главное 2021" проверяем, что оказались на странице /BEST
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_BEST)
      BEST_URL = self.authPage.get_url()
      assert BEST_URL == TestData.BEST_URL
      # нажимаем на логотип и проверяем, что оказались на главной странице
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      LOGO_URL = self.authPage.get_url()
      assert LOGO_URL == TestData.START_URL
      # нажимаем на "Рейтинг" проверяем, что оказались на странице /RATING
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_RATING)
      RATING_URL = self.authPage.get_url()
      assert RATING_URL == TestData.RATING_URL
      # нажимаем на логотип и проверяем, что оказались на главной странице
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      LOGO_URL = self.authPage.get_url()
      assert LOGO_URL == TestData.START_URL
      # нажимаем на "Что почитать" проверяем, что оказались на странице /TOP/TOREAD
      self.authPage.hover_cursor_click(AuthLocators.AUTH_TOP_TOREAD)
      TOP_TOREAD_URL = self.authPage.get_url()
      assert TOP_TOREAD_URL == TestData.TOP_TOREAD_URL
      # нажимаем на логотип и проверяем, что оказались на главной странице
      self.authPage.hover_cursor_click(AuthLocators.AUTH_LOGO)
      LOGO_URL = self.authPage.get_url()
      assert LOGO_URL == TestData.START_URL

   def test_add_to_cart_method_1(self):
      """Проверяем, что нажатие на кнопку "Корзина" в карточке товара добавлет товар в корзину, а нажатие
      на кнопку "Оформить" на всплывающем окне переводит в корзину"""
      self.authPage = AuthPage(self.driver)

      # проверяем количество книг в корзине
      CART_PAGE_BOOKS_NUMBER = int(self.authPage.get_element_text(AuthLocators.AUTH_HEADER_BUTTON_ICONS_CART_NUMBER))

      # Ищем фото первой книги
      START_PAGE_BOOK_IMG = self.authPage.element_are_present(
         AuthLocators.AUTH_START_PAGE_BOOKS_IMG)
      # записываем в переменную значение атрибута title у первой книги
      START_PAGE_BOOK_IMG_TITLE = self.authPage.get_attribute_value(AuthLocators.AUTH_START_PAGE_BOOKS_IMG, TestData.attribut_img_title)

      # проверяем невидимость на странице окна "Оформить"
      POP_UP_WINDOW_CHECK_OUT = self.authPage.element_are_present(
         AuthLocators.AUTH_POP_UP_WINDOW_CHECK_OUT)
      assert POP_UP_WINDOW_CHECK_OUT.is_displayed() == False

      # скроллим до элемента (фото книги)
      self.authPage.scroll_to_element(START_PAGE_BOOK_IMG)
      # наводим курсор на кнопку "В КОРЗИНУ" у первой книги и нажимаем, проверяем появление на дисплее окна "Оформить"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_PAGE_BOOKS_BTN_CART)
      assert POP_UP_WINDOW_CHECK_OUT.is_displayed()
      # Нажимаем на кнопку "Оформить" всплывающего окна "Оформить", проверяем, что кнопка перевела на страницу /cart
      self.authPage.hover_cursor_click(AuthLocators.AUTH_POP_UP_WINDOW_BTN_CHECK_OUT)
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL

      # проверяем,что в корзину добавился 1 элемент
      CART_PAGE_BOOKS = self.authPage.all_elements_are_presents(
         AuthLocators.AUTH_CART_PAGE_BOOKS_IMG)
      assert len(CART_PAGE_BOOKS) == CART_PAGE_BOOKS_NUMBER + 1

      # проверяем,что название заглавий в атрибутах у элемена на стартовой странице и у первого элемента в корзине совпадает
      CART_PAGE_BOOK_IMG_TITLE = self.authPage.get_attribute_value(AuthLocators.AUTH_CART_PAGE_BOOKS_IMG, TestData.attribut_img_title)
      assert CART_PAGE_BOOK_IMG_TITLE == START_PAGE_BOOK_IMG_TITLE


   def test_add_to_cart_method_2(self):
      """Проверяем, что нажатие на кнопку "Корзина" в карточке товара добавлет товар в корзину"""
      self.authPage = AuthPage(self.driver)

      # проверяем количество книг в корзине
      CART_PAGE_BOOKS_NUMBER = int(self.authPage.get_element_text(AuthLocators.AUTH_HEADER_BUTTON_ICONS_CART_NUMBER))

      # Ищем фото первой книги
      START_PAGE_BOOK_IMG = self.authPage.element_are_present(
         AuthLocators.AUTH_START_PAGE_BOOKS_IMG)
      # записываем в переменную значение атрибута title у первой книги
      START_PAGE_BOOK_IMG_TITLE = self.authPage.get_attribute_value(AuthLocators.AUTH_START_PAGE_BOOKS_IMG, TestData.attribut_img_title)

      # скроллим до элемента (фото книги)
      self.authPage.scroll_to_element(START_PAGE_BOOK_IMG)
      # наводим курсор на кнопку "В КОРЗИНУ" у первой книги и нажимаем, проверяем, что название сменилось на "ОФОРМИТЬ"
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_PAGE_BOOKS_BTN_CART)
      TEXT_BOOKS_BTN_CART = self.authPage.get_element_text(AuthLocators.AUTH_START_PAGE_BOOKS_BTN_CART)
      assert TEXT_BOOKS_BTN_CART == "ОФОРМИТЬ"

      # повторным кликом на кнопку "ОФОРМИТЬ" переходим на страницу /cart, проверяем это по URL
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_PAGE_BOOKS_BTN_CART)
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL

      # проверяем,что в корзину добавился 1 элемент
      CART_PAGE_BOOKS = self.authPage.all_elements_are_presents(
         AuthLocators.AUTH_CART_PAGE_BOOKS_IMG)
      assert len(CART_PAGE_BOOKS) == CART_PAGE_BOOKS_NUMBER + 1

      # проверяем,что название заглавий в атрибутах у элемена на стартовой странице и у первого элемента в корзине совпадает
      CART_PAGE_BOOK_IMG_TITLE = self.authPage.get_attribute_value(AuthLocators.AUTH_CART_PAGE_BOOKS_IMG,
                                                                   TestData.attribut_img_title)
      assert CART_PAGE_BOOK_IMG_TITLE == START_PAGE_BOOK_IMG_TITLE



   def test_add_to_cart_method_3(self):
      """Проверяем, что нажатие на кнопку "Корзина" в карточке товара добавлет товар в корзину, нажатие
      на иконку "КОРЗИНА в шапке сайта переводит в корзину"""
      self.authPage = AuthPage(self.driver)

      # проверяем количество книг в корзине
      CART_PAGE_BOOKS_NUMBER = int(self.authPage.get_element_text(AuthLocators.AUTH_HEADER_BUTTON_ICONS_CART_NUMBER))

      # Ищем фото первой
      START_PAGE_BOOK_IMG = self.authPage.element_are_present(
         AuthLocators.AUTH_START_PAGE_BOOKS_IMG)
      # записываем в переменную значение атрибута title у первой книги
      START_PAGE_BOOK_IMG_TITLE = self.authPage.get_attribute_value(AuthLocators.AUTH_START_PAGE_BOOKS_IMG,
                                                                    TestData.attribut_img_title)
      # скроллим до элемента (фото книги)
      self.authPage.scroll_to_element(START_PAGE_BOOK_IMG)
      # наводим курсор на кнопку "В КОРЗИНУ" у первой книги и нажимаем
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_PAGE_BOOKS_BTN_CART)

      # Скроллим до кнопки "КОРЗИНА" в шапке сайта и нажимаем, проверяем, что кнопка перевела на страницу /cart
      HEADER_BUTTON_CART = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_CART)
      self.authPage.scroll_to_element(HEADER_BUTTON_CART)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_CART)
      CART_URL = self.authPage.get_url()
      assert CART_URL == TestData.CART_URL

      # проверяем,что в корзину добавился 1 элемент
      CART_PAGE_BOOKS = self.authPage.all_elements_are_presents(
         AuthLocators.AUTH_CART_PAGE_BOOKS_IMG)
      assert len(CART_PAGE_BOOKS) == CART_PAGE_BOOKS_NUMBER + 1

      # проверяем,что название заглавий в атрибутах у элемена на стартовой странице и у первого элемента в корзине совпадает
      CART_PAGE_BOOK_IMG_TITLE = self.authPage.get_attribute_value(AuthLocators.AUTH_CART_PAGE_BOOKS_IMG,
                                                                   TestData.attribut_img_title)
      assert CART_PAGE_BOOK_IMG_TITLE == START_PAGE_BOOK_IMG_TITLE


   def test_start_page_add_to_favorites(self):
      """Проверяем возможность добавить книгу в избранное"""
      self.authPage = AuthPage(self.driver)
      # принимает cookies и закрывает окно
      self.authPage.accept_cookies_btn()

      # Ищем иконки "отложить", скроллим до первой иконки (иконки у первой книги) и наводим на нее курсор и нажимаем
      START_PAGE_BOOKS_BTN_FAVOURITES = self.authPage.all_elements_are_presents(
         AuthLocators.AUTH_START_PAGE_BOOKS_FAVOURITES)
      self.authPage.scroll_to_element(START_PAGE_BOOKS_BTN_FAVOURITES[0])
      self.authPage.hover_cursor_click(AuthLocators.AUTH_START_PAGE_BOOKS_FAVOURITES)

      # Скролл до шапки сайта, наводим курсор на иконку "Отложено" и нажимаем ее
      HEADER_BUTTON_PUTORDER = self.authPage.element_are_present(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)
      self.authPage.scroll_to_element(HEADER_BUTTON_PUTORDER)
      self.authPage.hover_cursor_click(AuthLocators.AUTH_HEADER_BUTTON_PUTORDER)

      # открывается страница "Отложенные", получаем URL новой страницы и сравниваем с данными из config.py
      PUTORDER_URL = self.authPage.get_url()
      assert PUTORDER_URL == TestData.PUTORDER_URL

      # ищем все элементы-книги на страницу, проверяем, что количество эелемтов на странице = 1
      START_PAGE_BOOKS = self.authPage.all_elements_are_presents(AuthLocators.AUTH_START_PAGE_BOOKS)
      assert len(START_PAGE_BOOKS) == 1