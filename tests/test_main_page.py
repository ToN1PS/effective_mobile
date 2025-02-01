import pytest
import allure
from pages.main_page import MainPage

@pytest.fixture
def main_page(page):
    return MainPage(page)

@pytest.mark.parametrize("link, expected_url", [
    ("about_us", "/#about"),
    ("services", "/#moreinfo"),
    ("projects", "/#cases"),
    ("reviews", "/#Reviews"),
    ("contacts", "/#contacts"),
])
def test_navigation_links(main_page: MainPage, link, expected_url):
    """
    Тест проверяет корректность переходов по ссылкам на главной странице.
    """
    main_url = "https://effective-mobile.ru"
    full_url = main_url + expected_url

    with allure.step(f"Переход на главную страницу {main_url}"):
        main_page.navigate(main_url)

    with allure.step(f"Клик по ссылке {link}"):
        getattr(main_page, f"click_{link}")()

    with allure.step(f"Проверка, что текущий URL равен {full_url}"):
        assert main_page.get_current_url() == full_url