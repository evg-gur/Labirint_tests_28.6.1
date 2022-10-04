from selenium.webdriver.common.by import By


class AuthLocators:
    # локатор логотипа "Лабиринт"
    AUTH_LOGO = (By.CLASS_NAME, "b-header-b-logo-e-logo")

    # Локатор блоков товаров-книг на стартовой на странице
    AUTH_START_PAGE_BOOKS = (By.CLASS_NAME, "product-padding")
    # Локатор фото товаров-книг на стартовой на странице
    AUTH_START_PAGE_BOOKS_IMG = (By.XPATH, '//div/a/span/img[@class="book-img-cover"]')
    # Локатор названий товаров-книг на стартовой на странице
    AUTH_START_PAGE_BOOKS_NAME = (By.CLASS_NAME, "product-title")
    # Локатор цены товаров-книг на стартовой на странице
    AUTH_START_PAGE_BOOKS_PRICE = (By.CLASS_NAME, "price-val")
    # Локатор значка "сердечко" (добавить в избранное) в блоках товаров-книг на стартовой на странице
    AUTH_START_PAGE_BOOKS_FAVOURITES = (By.XPATH, '//a[@data-tooltip_title="Отложить"]/span[@class="header-sprite"]')
    AUTH_START_PAGE_BOOKS_FAVOURITES_END = (By.XPATH, '//a[@data-tooltip_title="Отложить"]/span[@class="header-sprite"]')
    # Локатор кнопки "В Корзину" в блоках товаров-книг на стартовой на странице
    AUTH_START_PAGE_BOOKS_BTN_CART = (By.CLASS_NAME, "buy-avaliable")

    # локатор 5 кнопок в шапке сайта: "Позвонить", "Сообщения", "Мой Лабиринт", "Отложено", "Корзина"
    AUTH_HEADER_BUTTONS = (By.CLASS_NAME, "b-header-b-personal-e-list-item")
    # локатор кнопки "Отложено" в шапке сайта
    AUTH_HEADER_BUTTON_PUTORDER = (By.XPATH, '//a/span[text()="Отложено"]')
    # локатор кнопки "Корзина" в шапке сайта
    AUTH_HEADER_BUTTON_CART = (By.XPATH, '//a/span[text()="Корзина"]')
    # локатор кнопки "Мой Лабиринт"
    AUTH_HEADER_BUTTON_MY_LABIRINT = (By.XPATH, '//span[@style="white-space: normal;"]')
    # локатор кнопки "Позвонить" в шапке сайта
    AUTH_HEADER_BUTTON_CALL = (By.XPATH, '//a/span[text()="Позвонить"]')
    # локатор кнопки "Сообщения" в шапке сайта
    AUTH_HEADER_BUTTON_MESSAGES = (By.XPATH, '//a/span[text()="Сообщения"]')

    # локатор всех 4 верхних иконок в шапке сайта: "Позвонить", "Мой Лабиринт", "Отложено", "Корзина"
    AUTH_HEADER_BUTTON_ICONS = (By.CLASS_NAME, "b-header-b-personal-e-wrapper-m-closed")
    # локатор иконки в шапке сайта: "Позвонить"
    AUTH_HEADER_BUTTON_ICONS_CALL = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-call")
    # локатор иконки в шапке сайта: "Мой Лабиринт"
    AUTH_HEADER_BUTTON_ICONS_MY_LABIRINT = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-profile")
    # локатор иконки в шапке сайта: "Отложено"
    AUTH_HEADER_BUTTON_ICONS_PUTORDER = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-putorder")
    # локатор иконки в шапке сайта: "Корзина"
    AUTH_HEADER_BUTTON_ICONS_CART = (By.CLASS_NAME, "b-header-b-personal-e-icon-count-m-cart")
    # локатор числа в иконке в шапке сайта: "Корзина"
    AUTH_HEADER_BUTTON_ICONS_CART_NUMBER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    # локатор иконки в шапке сайта: "Сообщения"
    AUTH_HEADER_BUTTON_ICONS_MESSAGES = (By.CLASS_NAME, "b-header-b-personal-e-icon-m-news")
    # локатор формы регистрации "Мой лабиринт"
    AUTH_REGISTRATION_FORM_MY_LABIRINT = (By.CLASS_NAME, "lab-modal-content")

    # локатор фото книг на странице "Корзина"
    AUTH_CART_PAGE_BOOKS_IMG = (By.XPATH, '//span[@class="relative"]/img')

    # локатор кнопки "Главное 2021" в шапке сайта
    AUTH_HEADER_BUTTON_BEST = (By.XPATH, '//span[@class="b-header-b-menu-e-link"]/a[text()="Главное 2021"]')
    # локатор кнопки "Рейтинг" в меню под шапкой сайта
    AUTH_HEADER_BUTTON_RATING = (By.XPATH, '//a[text()="Рейтинги"]')
    # локатор кнопки "Что почитать..." на главной странице сайта
    AUTH_TOP_TOREAD = (By.XPATH, '//a[text()="Что почитать: выбор редакции"]')


    # шапка сайта: локатор всплывающего окна кнопки "Отложено"
    AUTH_POP_UP_WINDOW_PUTORDER = (By.XPATH, '//div[@class="b-menu-list-title font_regular tac"]')
    # шапка сайта: окатор всплывающего окна кнопки "Мой лабиринт"
    AUTH_POP_UP_WINDOW_MY_LABIRINT = (By.CLASS_NAME, "b-header-login-action-logo-e-wrap")
    # шапка сайта: локатор всплывающего окна кнопки "Корзина"
    AUTH_POP_UP_WINDOW_CART = (By.XPATH, '//li//div[@class="b-basket-popinfo-e-block b-basket-empty"]')
    # шапка сайта: локатор всплывающего окна кнопки "Сообщения"
    AUTH_POP_UP_WINDOW_MESSAGES = (By.XPATH, '//div[@class="b-header-login-e-enter"]/div[@class="b-menu-list-title font_regular"]')
    # шапка сайта: локатор всплывающего окна кнопки "Позвонить"
    AUTH_POP_UP_WINDOW_CALL = (
    By.XPATH, '//li[@class="b-header-b-personal-e-list-item b-header-b-personal-e-list-item-m-sm first-child have-dropdown"]/div/div[@class="popup-window-content b-basket-popinfo"]')


    # локатор кнопки "Принять" cookies
    AUTH_ACCEPT_COOKIES_BTN = (By.CLASS_NAME, 'cookie-policy__button')

    # локатор формы авторизации
    AUTH_AUTHORIZATION_WINDOW = (By.CLASS_NAME, 'lab-modal-content')

    # локатор всплывающего окна "Оформить" (после нажатия на кнопку "В КОРЗИНУ")
    AUTH_POP_UP_WINDOW_CHECK_OUT = (By.XPATH, '//div[@class="popup-window top-block-popup basket-popup b-basket-info-popup"]')
    # локатор кнопки "Оформить" всплывающего окна "Оформить" (после нажатия на кнопку "В КОРЗИНУ")
    AUTH_POP_UP_WINDOW_BTN_CHECK_OUT = (By.XPATH, '//div[@class="b-basket-popinfo-e-text-row"]/a[text()="Оформить"]')

    # локатор строки поиска
    AUTH_SEARCH_FIELD = (By.ID, "search-field")
    # локатор иконки поиска
    AUTH_ICON_SEARCH_FIELD = (By.XPATH, '//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]')
    # локатор всплывающего окна поиска "ВЫ ИСКАЛИ"
    AUTH_POP_UP_SEARCH_FIELD = (By.XPATH, '//span[text()="ВЫ ИСКАЛИ"]')
    AUTH_POP_UP_SEARCH_FIELD_3 = (By.XPATH, '//div[@class="b-suggests-block b-suggests-block-m-nopadding"]')
    AUTH_POP_UP_SEARCH_FIELD_1 = (By.XPATH, '//div[@class="b-suggests-thumbs-outer b-header-b-tinyscrollbar"]')
    AUTH_POP_UP_SEARCH_FIELD_2 = (By.XPATH, '//div[@class="b-suggests-thumbs-outer b-header-b-tinyscrollbar"]/div')
    # локатор кнопики "Очистить всю историю поиска" всплывающего окна поиска "ВЫ ИСКАЛИ"
    AUTH_POP_UP_SEARCH_FIELD_CLEAR_HISTORY = (By.XPATH, '//span[@class="b-suggests-item pointer js-suggests-del"]')
    AUTH_POP_UP_SEARCH_FIELD_CLEAR_HISTORY_1 = (By.XPATH, '//span[text()="Очистить всю историю поиска"]')
    # локатор всплывающего окна поиска "ЧТО ИЩУТ"
    AUTH_POP_UP_SEARCH_FIELD_WHAT_THEY_LOOKING = (By.XPATH, '//span[text()="ЧТО ИЩУТ"]')

    # локатор заголовка с результатами поиска
    AUTH_TITLE_SEARCH_RESULT = (By.CLASS_NAME, "index-top-title")

    # локатор всех книг, найденых по параметру поиска
    AUTH_SEARCH_BOOKS = (By.XPATH, '//div[@class="product need-watch watched"]')
    # локатор книги "Три мушкетера" А.Дюма
    AUTH_BOOK_TRI_MUSKETEERS = (By.XPATH, '//div[@data-product-id="606809"]')
    # локатор кнопки "Следующая" для перехода на следующую страницу поиска
    AUTH_SEARCH_BTN_NEXT_PAGE = (By.XPATH, '//div[@class="pagination-next"]/a[text()="Следующая"]')
    AUTH_SEARCH_BTN_NEXT_PAGE_3 = (By.XPATH, '//div[@class="pagination-next"]/a[@class="pagination-next__text"]')
    AUTH_SEARCH_BTN_NEXT_PAGE_1 = (By.XPATH, '//div[@class="pagination pushstate"]')
    AUTH_SEARCH_BTN_NEXT_PAGE_2 = (By.XPATH, '//div[@class="products-row "]')
    # локатор общего количества найденных книг
    AUTH_TOTAL_NUMBER_SEARCH_BOOKS = (By.XPATH, '//li[@class="b-stab-e-slider-item b-stab-e-slider-item-m-active "]/a/span[@class="b-stab-e-slider-item-e-txt-m-small js-search-tab-count"]')
    AUTH_TOTAL_NUMBER_SEARCH_BOOKS_1 = (By.XPATH,
                                      '//li[@class="b-stab-e-slider-item b-stab-e-slider-item-m-active b-stab-e-slider-item-m-last"]/a/span[@class="b-stab-e-slider-item-e-txt-m-small js-search-tab-count"]')

    # локаторы формы доступа в "Мой Лабиринт"
    # локатор поля ввода
    AUTH_ACCESS_INPUT_FIELD = (By.XPATH, '//input[@autocomplete="code tel email phone phones telephone mail"]')
    # локатор кнопки "Войти"
    AUTH_ACCESS_BTN_LOGIN = (By.ID, 'g-recap-0-btn')
    # локатор комментария к полю ввода
    AUTH_ACCESS_INPUT_FIELD_COMMENT = (By.XPATH, '//span[@data-default-text="Найдем вас в Лабиринте или зарегистрируем"]')
    # локатор комментария к полю ввода после нажатия "Войти"
    AUTH_ACCESS_INPUT_FIELD_COMMENT_ENTER = (By.XPATH, '//small[text()="Введенного кода не существует"]')
    # локатор комментария о звонке на номер
    AUTH_ACCESS_BTN_LOGIN_COMMENT_CALL = (By.XPATH, '//small[text()="В течение 1 минуты на "]/span[@class="js-replace-phone"]')


