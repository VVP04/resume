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

    assert "home.html" in [
        template.name for template in response.templates
    ]

    assert 'Владимир Плесовских' in response.content.decode()
    assert 'Резюме' in response.content.decode()


@pytest.mark.xfail(reason='Кнопки ещё не подключены, URL не созданы')
def test_home_buttons(client):
    response = client.get(reverse('home'))
    content = response.content.decode()


    portfolio_url = reverse('portfolio_list')
    contacts_url = reverse('contacts')
    assert portfolio_url in content
    assert contacts_url in content


    assert client.get(portfolio_url).status_code == 200
    assert client.get(contacts_url).status_code == 200


@pytest.mark.django_db
def test_about_page(client):
    url = reverse('about')

    response = client.get(url)

    assert response.status_code == 200

    assert "about.html" in [
        template.name for template in response.templates
    ]

    content = response.content.decode()

    assert "Владимир Плесовских" in content
    assert "Обо мне" in content
    assert "О моих интересах, образовании и направлениях профессионального развития." in content

    assert "vova.plesovkikh@gmail.com" in content
    assert "+7 912 922-94-71" in content
    assert "Россия, Екатеринбург" in content

    assert "Разработка" in content
    assert "Маркетинг" in content
    assert "Аналитика" in content

    assert "Мои направления" in content
    assert "Python и Django" in content
    assert "Яндекс Директ" in content
    assert "VK Рекламой" in content

    assert "Специализация" in content
    assert "Образование" in content
    assert "Опыт" in content


@pytest.mark.xfail(reason='Кнопки ещё не подключены, URL не созданы')
def test_about_buttons(client):
    response = client.get(reverse('about'))
    content = response.content.decode()

    contacts_url = reverse('contacts')
    assert contacts_url in content

    assert client.get(contacts_url).status_code == 200