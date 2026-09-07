import pytest
from bs4 import BeautifulSoup
from django.urls import reverse
from .models import SkillCategory, Skill, Education, Experience


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


@pytest.mark.django_db
def test_resume_page_returns_200(client):
    response = client.get(reverse('resume'))

    assert response.status_code == 200


@pytest.mark.django_db
def test_resume_page_uses_correct_template(client):
    response = client.get(reverse("resume"))

    assert "resume.html" in [
        template.name for template in response.templates
    ]


@pytest.mark.django_db
def test_resume_page_displays_profile(client):
    response = client.get(reverse("resume"))

    content = response.content.decode()

    assert "Резюме" in content
    assert (
        "Мой профессиональный опыт, " 
        "ключевые навыки и стек технологий" 
        in content
    )
    assert "Владимир Плесовских" in content


@pytest.mark.django_db
def test_resume_page_displays_skills(client):
    category = SkillCategory.objects.create(
        name="Backend",
    )

    Skill.objects.create(
        name="Python",
        category=category,
    )

    Skill.objects.create(
        name="Django",
        category=category,
    )

    response = client.get(reverse("resume"))

    content = response.content.decode()

    assert "Backend" in content
    assert "Python" in content
    assert "Django" in content


@pytest.mark.django_db
def test_resume_page_displays_higher_educations(client):
    Education.objects.create(
        specialty="Международный и корпоративный менеджмент",
        degree="Бакалавриат",
        start_year=2022,
        end_year=2026,
        institution="Уральский федеральный университет",
        description=(
            "Профиль «Маркетинг». Изучение менеджмента, маркетинга, "
            "бизнес-аналитики и управления."
        ),
        education_type="higher",
    )

    Education.objects.create(
        specialty=(
            "Интеллектуальные информационные системы и технологии "
            "в медицине"
        ),
        degree="Магистратура",
        start_year=2026,
        end_year=2028,
        institution="Уральский федеральный университет",
        description=(
            "Поступил в магистратуру в 2026 году. "
            "Планируемое окончание — 2028 год."
        ),
        education_type="higher",
    )

    response = client.get(reverse("resume"))
    
    content = response.content.decode()

    assert "Международный и корпоративный менеджмент" in content
    assert "Бакалавриат" in content
    assert "2022 — 2026" in content
    assert "Уральский федеральный университет" in content
    assert "Профиль «Маркетинг»" in content

    assert (
        "Интеллектуальные информационные "
        "системы и технологии в медицине"
        in content
    )
    assert "Магистратура" in content
    assert "2026 — 2028" in content
    assert "Поступил в магистратуру в 2026 году" in content


@pytest.mark.django_db
def test_resume_page_displays_additional_education(client):
    Education.objects.create(
        specialty="Python-разработчик",
        degree="Курсы",
        start_year=2024,
        end_year=2025,
        institution="Hexlet",
        description=(
            "Освоение разработки на Python: объектно-ориентированное "
            "программирование, Django, базы данных, Git и автоматизированное "
            "тестирование."
        ),
        education_type="additional",
    )

    Education.objects.create(
            specialty="Продакт-менеджер",
            degree="Профессиональная переподготовка",
            start_year=2024,
            end_year=2025,
            institution="Уральский Федеральный Университет",
            description=(
                "Профессиональная переподготовка в области управления "
                "IT-продуктами: развитие продукта, анализ требований, "
                "работа с пользователями и управление продуктовой командой."
            ),
            education_type="additional",
        )

    response = client.get(reverse("resume"))
    
    content = response.content.decode()

    assert "Python-разработчик" in content
    assert "Курсы" in content
    assert "2024 — 2025" in content
    assert "Hexlet" in content
    assert "Освоение разработки на Python" in content

    assert "Продакт-менеджер" in content
    assert "Профессиональная переподготовка" in content
    assert "Уральский Федеральный Университет" in content
    assert "Профессиональная переподготовка в области управления" in content


@pytest.mark.django_db
def test_resume_page_experience(client):
    Experience.objects.create(
        position="Ученик курса \"Python-разработчик\"",
        company="Hexlet",
        start_year=2024,
        end_year=2025,
        description=(
            "Изучение Python и объектно-ориентированного программирования.\n"
            "Разработка приложений на Django.\n"
            "Работа с базами данных и Git.\n"
            "Написание автоматизированных тестов."
        ),
    )

    response = client.get(reverse("resume"))
        
    content = response.content.decode()

    assert "Ученик курса" in content
    assert "Python-разработчик" in content
    assert "Hexlet" in content
    assert "2024 — 2025" in content

    assert "Изучение Python и объектно-ориентированного программирования" in content
    assert "Разработка приложений на Django" in content
    assert "Работа с базами данных и Git" in content
    assert "Написание автоматизированных тестов" in content


@pytest.mark.xfail(reason="URL для кнопок ещё не подключены")
def test_resume_page_download_resume(client):
    response = client.get(reverse("resume"))

    soup = BeautifulSoup(response.content, "html.parser")

    resume_buttons = soup.select_one(".resume-buttons")

    assert resume_buttons is not None

    download_link = resume_buttons.select_one(
        f"a[href='{reverse('download_resume')}']"
    )

    assert download_link is not None
    assert download_link.get_text(strip=True) == "Скачать резюме"