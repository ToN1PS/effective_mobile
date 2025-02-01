# 📌 Проект: Автоматизированное тестирование UI с Playwright и Allure

## 📖 Описание
Этот проект предназначен для автоматизированного тестирования UI с использованием **Playwright**, **pytest** и генерации отчетов в **Allure**. Запуск и управление тестами осуществляется в **Docker**.

## 🚀 Установка и запуск

### 🔹 1. Клонирование репозитория
```bash
git clone <репозиторий>
cd <папка проекта>
```

### 🔹 2. Установка зависимостей
Создай и активируй виртуальное окружение (необязательно, если используешь Docker):
```bash
python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

### 🔹 3. Запуск тестов
#### 🏃 Без Docker:
```bash
pytest --alluredir=allure-results
```

#### 🏃 В Docker:
```bash
docker build -t test-container .
docker run --rm -v $(pwd)/allure-results:/app/allure-results test-container
```

### 🔹 4. Просмотр отчетов Allure
#### 📊 Локальный сервер:
```bash
allure serve allure-results
```

#### 📊 Генерация статического отчета:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

#### 📊 Запуск Allure в Docker Compose:
```bash
docker-compose up -d
```
Открой отчет в браузере: `http://localhost:5050`

## 🛠 Docker команды
### 🔹 Запуск контейнера
```bash
docker-compose up -d
```
### 🔹 Остановка контейнера
```bash
docker-compose down
```
### 🔹 Проверка запущенных контейнеров
```bash
docker ps
```
### 🔹 Подключение к контейнеру
```bash
docker exec -it <container_id> sh
```

## 🔗 Полезные ссылки
- [Playwright Docs](https://playwright.dev/)
- [pytest Docs](https://docs.pytest.org/)
- [Allure Docs](https://docs.qameta.io/allure/)
- [Docker Docs](https://docs.docker.com/)

