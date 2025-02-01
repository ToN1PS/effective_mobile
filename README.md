# Проект: Автоматизированное тестирование UI с использованием Playwright и Allure

<p align="center">
  <img src="image-1.png" alt="alt text" />
  <img src="image-2.png" alt="alt text" />
</p>

## Описание
Данный проект предназначен для автоматизированного тестирования пользовательского интерфейса с использованием **Playwright** и **pytest**, а также для формирования отчетов в **Allure**. Запуск и управление тестами осуществляется посредством **Docker**.

Проект включает тесты, проверяющие основные разделы веб-приложения, включая корректность навигации и отображения контента. Все тесты реализованы с использованием паттерна Page Object Model (POM) для удобства поддержки и расширяемости.

----

## Требования
Перед началом работы убедитесь, что на вашей системе установлены:
- **Python 3.10** или выше
- **Docker** и **Docker Compose**
- **Google Chrome** или другой поддерживаемый браузер

----

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/ToN1PS/effective_mobile.git
cd effective_mobile
```

### 2. Установка зависимостей
При использовании виртуального окружения (необязательно при запуске через Docker):
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Запуск тестов
#### Запуск без Docker:
```bash
python -m pytest --alluredir=allure-results
```

#### Запуск в Docker:
1. Запуск Allure backend.
2. Запуск Allure UI.
3. Запуск тестов и передача результатов в Allure backend.
```bash
docker compose up
```

### 4. Просмотр отчетов Allure
#### Доступ к отчету на локальном сервере:
После успешного запуска контейнеров отчет будет доступен в веб-браузере.

🔗 Перейдите по адресу: http://localhost:5252

📌 Важно: Отчет становится доступным только после выполнения команды docker compose up и завершения тестов.

----

## Полезные ссылки
- [Документация Playwright](https://playwright.dev/)
- [Документация pytest](https://docs.pytest.org/)
- [Документация Allure](https://docs.qameta.io/allure/)
- [Документация Docker](https://docs.docker.com/)
