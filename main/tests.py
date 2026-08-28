import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


@pytest.mark.xfail(reason="URL ещё не подключены")
def test_sidebar_navigation_links(client):
    response = client.get(reverse("home"))

    soup = BeautifulSoup(response.content, "html.parser")

    sidebar = soup.select_one(".sidebar")

    assert sidebar is not None

    home_link = sidebar.select_one(
        f"a[href='{reverse('home')}']"
    )
    assert home_link is not None
    assert home_link.get_text(strip=True) == "Главная"

    about_link = sidebar.select_one(
        f"a[href='{reverse('about')}']"
    )
    assert about_link is not None
    assert about_link.get_text(strip=True) == "Обо мне"

    resume_link = sidebar.select_one(
        f"a[href='{reverse('resume')}']"
    )
    assert resume_link is not None
    assert resume_link.get_text(strip=True) == "Резюме"

    portfolio_link = sidebar.select_one(
        f"a[href='{reverse('portfolio_list')}']"
    )
    assert portfolio_link is not None
    assert portfolio_link.get_text(strip=True) == "Портфолио"

    contacts_link = sidebar.select_one(
        f"a[href='{reverse('contacts')}']"
    )
    assert contacts_link is not None
    assert contacts_link.get_text(strip=True) == "Контакты"


def test_homepage_returns_200(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200


def test_homepage_uses_correct_template(client):
    response = client.get(reverse("home"))

    assert "home.html" in [
        template.name for template in response.templates
    ]


def test_homepage_displays_content(client):
    response = client.get(reverse("home"))

    content = response.content.decode()

    assert "Владимир Плесовских" in content
    assert "Резюме" in content


@pytest.mark.xfail(reason="URL для кнопок ещё не подключены")
def test_home_page_hero_links(client):
    response = client.get(reverse("home"))

    soup = BeautifulSoup(response.content, "html.parser")

    hero_buttons = soup.select_one(".hero-buttons")

    assert hero_buttons is not None

    portfolio_link = hero_buttons.select_one(
        f"a[href='{reverse('portfolio_list')}']"
    )
    assert portfolio_link is not None
    assert portfolio_link.get_text(strip=True) == "Мои работы"

    contacts_link = hero_buttons.select_one(
        f"a[href='{reverse('contacts')}']"
    )
    assert contacts_link is not None
    assert contacts_link.get_text(strip=True) == "Связаться со мной"


def test_about_page_returns_200(client):
    response = client.get(reverse("about"))

    assert response.status_code == 200


def test_about_page_uses_correct_template(client):
    response = client.get(reverse("about"))

    assert "about.html" in [
        template.name for template in response.templates
    ]


def test_about_page_displays_content(client):
    response = client.get(reverse("about"))

    content = response.content.decode()

    assert "Владимир Плесовских" in content
    assert "Обо мне" in content
    assert (
        "О моих интересах, образовании и направлениях "
        "профессионального развития."
        in content
    )

    assert "Разработка" in content
    assert "Маркетинг" in content
    assert "Аналитика" in content

    assert "Специализация" in content
    assert "Язык" in content
    assert "Образование" in content
    assert "Опыт" in content


@pytest.mark.xfail(reason="URL для кнопок ещё не подключены")
def test_about_page_contact_links(client):
    response = client.get(reverse("about"))

    soup = BeautifulSoup(response.content, "html.parser")

    about_buttons = soup.select_one(".about-buttons")

    assert about_buttons is not None

    contact_link = about_buttons.select_one(
        f"a[href='{reverse('contacts')}']"
    )

    assert contact_link is not None
    assert contact_link.get_text(strip=True) == "Обсудить проект"