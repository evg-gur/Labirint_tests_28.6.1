class TestData:
    # АДРЕС ДРАЙВЕРА
    CHROME_DRIVER_PATH = 'C:\\driver\\chromedriver.exe'
    # URL стартовой страницы "Лабиринт"
    START_URL = 'https://www.labirint.ru/'

    # URL страниц кнопок/иконок в шапке сайта
    PUTORDER_URL = START_URL + 'cabinet/putorder/'
    CART_URL = START_URL + 'cart/'
    CALL_URL = START_URL + 'contact/'

    # URL страниц ссылок в шапке сайта
    BEST_URL = START_URL + 'best/'
    SCHOOL_URL = START_URL + 'school/'
    GAMES_URL = START_URL + 'games/'
    OFFICE_URL = START_URL + 'office/'
    CLUB_URL = START_URL + 'club/'

    # URL страниц разделов в поле под шапкой сайта
    DELIVERY_URL = START_URL + 'help/'
    SERTIFICATES_URL = START_URL + 'top/certificates/'
    RATING_URL = START_URL + 'rating/?id_genre=-1&nrd=1'
    NOVELTY_URL = START_URL + 'novelty/'
    DISCOUNT_URL = START_URL + 'search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'
    CONTACT_URL = START_URL + 'contact/'
    SUPPORT_URL = START_URL + 'support/'
    MAPS_URL = START_URL + 'maps/'
    MOSCOW_DELIVERY_URL = MAPS_URL

    # URL страниц ссылок на главной странице сайта
    TOP_TOREAD_URL = START_URL + 'top/toread/'

    TEXT_BASE_PAGE = 'u"Лучшая покупка дня"'

    # атрибуты карточки товара
    TEXT_BTN_CART = 'В КОРЗИНУ'
    TEXT_BTN_CART_1 = 'ПРЕДЗАКАЗ'
    IMG_attribute = 'src'

    # Параметры размера открываемой страницы на экране
    WIDTH_WINDOW_1 = 1020
    LENGTH_WINDOW_1 = 900
    WIDTH_WINDOW = 1900
    LENGTH_WINDOW = 1000

    # Параметры ввода текста
    text_search_1 = 'книги'
    text_search_2 = 'журналы'
    text_search_url = 'search'

    # название атрибута из локатора img для идентификаци книг
    attribut_img_title = 'title'

    # Параметры поиска книги А.Дюма "Три мушкетера"
    author_last_name_rus = 'Дюма'
    author_last_name_eng = 'Dumas'
    author_last_name_latin = 'L.vf'
    author_rus_initials_1 = 'А.Дюма'
    author_rus_initials_2 = 'А. Дюма'
    title_book_rus = 'Три мушкетера'
    title_book_eng = 'Three musketeers'
    title_book_latin = 'Nhb veirtnthf'
    title_book_first_part = 'три'
    title_book_end_part = 'мушкетера'
    title_book_topic = 'про мушкетеров'
    title_book_figure = '3'
    title_book_price = '1824'
    title_book_price_1 = '1800'
    title_book_id = '606809'

    # ID книги "Три мушкетера"
    ID_TRI_MUSKEETERS = '606809'
    # название атрибута ID книги "Три мушкетера"
    attribut_name = 'data-product-id'

    # параметры для ввода данных в строку поиска
    symbol_255 = 'РопбавовдачалаяыжввляюыьсчбтмсчмблмотсчлмочвблюсоячвбьстчсбьстчсьбтмсчьортмалворпалввыболдвколовыолдывоулдыжщщщблрролрлшгрогнерольлдщшщщджэхзщшгнРопбавовдачалаяыжввляюыьсчбтмсчмблмотсчлмочвблюсоячвбьстчсбьстчсьбтмсчьортмалворпалввыболдвколовыолдывоулдызхг'
    special_symbol = '@#$%^&*()_!@#'

    # данные для ввода в форму достуа в "Мой лабиринт"
    min_number = 10
    max_number = 50
    min_letters = 12
    max_letters = 50
    number = 1
    number_50 = 11111111111111111111111111111111111111111111111111
    number_60 = 111111111111111111111111111111111111111111111111111111111111
    letter_eng = 's'
    letter_rus = 'я'
    email = 'email@email.ru'
    email_incorrect = '1@2.ru'
    email_incorrect_1 = 'email@imail.email'

    # возможные комментарии к полю ввода
    comment_login = 'Найдем вас в Лабиринте или зарегистрируем'
    comment_symbol_cannot_used = 'Нельзя использовать символ'
    comment_input_language = 'Переключите язык ввода'
    attribut_input_string = 'maxlength'









