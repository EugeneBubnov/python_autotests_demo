# Api Testing Framework
[![Python](https://img.shields.io/badge/Python-3.14.2-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-orange)](https://docs.pytest.org/)
[![Requests](https://img.shields.io/badge/Requests-2.31%2B-yellow)](https://requests.readthedocs.io/)
[![Allure](https://img.shields.io/badge/Allure%20Report-2.24%2B-ff69b4)](https://allurereport.org/)

## Демо проекта по автоматизированному тестированию REST API.
Проект демонстрирует подход к построению архитектуры тестового фреймворка с разделением ответственности: 
* HTTP-клиент с логированием, который можно масштабировать под разные сервисы
* Сервисный слой для бизнес-логики
* Модели данных и изолированные тесты на pytest
* Реализован полный CRUD-сценарий жизненного цикла пользователя.
## Технологический стек
- **Python 3.14** — Язык программирования
- **pytest** — Тест-раннер
- **requests** — Библиотека для API-запросов
- **jsonpath** — Поиск данных в JSON-ответах
- **dataclasses** — Модели данных
- **faker** — Генерация тестовых данных
- **allure** — Система отчетности

## Запуск api-тестов

```bash
# Создание и активация виртуального окружения
python -m venv .venv
.venv\Scripts\activate

# Установка библиотек
pip install -r requirements.txt

# Запуск одного теста
pytest tests/social_api_suite/ --alluredir=allure-results

# Запуск тестов в параллельном режиме(если тестов больше, чем 1)
pytest tests/social_api_suite/ -n auto --alluredir=allure-results

# Генерация страницы с отчётом
allure serve 
```
## Отчёт:
![allure](demo_images/allure-image.png)

---