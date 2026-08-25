import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_homepage(client):
    url = reverse('home')

    response = client.get(url)

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