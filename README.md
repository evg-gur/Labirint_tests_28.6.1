# Labirint_tests_28.6.1

Итоговый проект по разделу «Автоматизация тестирования» в курсе "Тестировщик-автоматизатор на Python (QAP)" (Skillfactory) 
Необходимо написать 50-70 автоматизированных тестов с использованием PyTest и Selenium для тестирования интернет-магазина –  "Лабиринт" (https://www.labirint.ru/)

Файл "config" содержит:
путь к вебдрайверу; URL страниц сайта; параметры размера экрана; параметры для ввода данных; контрольные значения.

Файл "conftest" содержит:
фикстуру для настройки браузера (Google Chrome).

Папка "pages" содержит:
базовый класс ("base-page"); методы, которые используются в тестах (auth_page); все локаторы ("locators").

Папка "tests" содержит базовый тест и 50 тестов сайта:
21 тест для стартовой страницы ("test_home"),
22 теста для поля поиска в шапке сайта ("test_search"),
7 тестов для строки ввода в форме регистрации ("test_access").
