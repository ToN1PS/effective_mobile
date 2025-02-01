# Используем официальный образ Python версии 3.10 с минимальным набором пакетов (slim)
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера как /app
WORKDIR /app

# Копируем файл requirements.txt из локальной директории в рабочую директорию контейнера
COPY requirements.txt .

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Устанавливаем зависимости, перечисленные в requirements.txt, без кэширования пакетов
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Playwright (инструмент для автоматизации браузеров)
RUN playwright install

# Устанавливаем системные зависимости, необходимые для работы Playwright
RUN playwright install-deps

# Копируем весь исходный код из локальной директории в рабочую директорию контейнера
COPY . .

# Создаем директорию allure-results для хранения результатов тестов. Если директория уже существует, команда игнорирует ошибку
RUN mkdir allure-results || true

# Создаем директорию allure-reports для хранения отчетов. Если директория уже существует, команда игнорирует ошибку
RUN mkdir allure-reports || true

# Команда по умолчанию, которая запускается при старте контейнера:
# 1. Запускает тесты с помощью pytest и сохраняет результаты в allure-results
# 2. Запускает скрипт send_results.py для обработки результатов
CMD ["sh", "-c", "python -m pytest --alluredir=allure-results && python utils/send_results.py"]