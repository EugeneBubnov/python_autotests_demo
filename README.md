# Api Testing Framework
[![Python](https://img.shields.io/badge/Python-3.14.2-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-orange)](https://docs.pytest.org/)
[![Requests](https://img.shields.io/badge/Requests-2.31%2B-yellow)](https://requests.readthedocs.io/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-brightgreen)](https://playwright.dev/)
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
pip install -r requirements.txt

# Запуск одного теста
pytest tests/api/ --alluredir=allure-results

# Запуск тестов в параллельном режиме(если тестов больше, чем 1)
pytest tests/api/ -n auto --alluredir=allure-results

# Генерация страницы с отчётом
allure serve allure-results
```
## Отчёт:
![allure](demo_images/allure-image.png)

---