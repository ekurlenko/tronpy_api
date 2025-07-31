# TronPy API

Сервис для работы с блокчейном TRON, предоставляющий API для получения информации о кошельках и сохранения адресов в базе данных.

## Описание

Сервис предоставляет два основных эндпоинта:
- `POST /api/tron/info` - получение информации о кошельке (баланс, энергия, пропускная способность) и сохранение адреса в БД
- `GET /api/tron/` - получение списка сохраненных кошельков с поддержкой пагинации

## Технологии

- FastAPI - веб-фреймворк
- SQLAlchemy - ORM для работы с базой данных
- PostgreSQL - база данных
- TronPy - библиотека для работы с блокчейном TRON
- Pytest - фреймворк для тестирования

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd tronpy_api
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта:

```env
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=tronpy_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 4. Запуск базы данных

Используйте Docker Compose для запуска PostgreSQL:

```bash
docker-compose up -d
```

### 5. Запуск приложения

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Приложение будет доступно по адресу: http://localhost:8000

## API Документация

После запуска приложения документация API будет доступна по адресу:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Тестирование

### Запуск всех тестов

```bash
python -m pytest tests/ -v
```

### Запуск интеграционных тестов

```bash
python -m pytest tests/test_api_integration.py -v
```

### Запуск юнит-тестов

```bash
python -m pytest tests/test_database_unit.py -v
```

### Запуск тестов с покрытием

```bash
python -m pytest tests/ --cov=app --cov-report=html
```

## Структура тестов

### Интеграционные тесты (`tests/test_api_integration.py`)

- `test_post_info_by_address_success` - тест успешного POST запроса
- `test_post_info_by_address_not_found` - тест обработки несуществующего адреса
- `test_post_info_by_address_bad_address` - тест обработки некорректного адреса

### Юнит-тесты (`tests/test_database_unit.py`)

- `test_create_wallet_success` - тест создания кошелька в базе данных

## Использование API

### Получение информации о кошельке

```bash
curl -X POST "http://localhost:8000/api/tron/info" \
     -H "Content-Type: application/json" \
     -d '{"address": "TJRabPrwbZy45sbavfcjinPJC18kjpRTv8"}'
```

Ответ:
```json
{
  "balance": "100.0",
  "energy": 500,
  "bandwidth": 1000
}
```

### Получение списка кошельков

```bash
curl "http://localhost:8000/api/tron/?offset=0&limit=10"
```

Ответ:
```json
[
  {
    "id": 1,
    "address": "TJRabPrwbZy45sbavfcjinPJC18kjpRTv8"
  }
]
```

## Разработка

### Добавление новых тестов

1. Создайте новый файл в директории `tests/`
2. Используйте фикстуры из `tests/conftest.py`
3. Следуйте существующим паттернам именования и структуры

### Структура проекта

```
tronpy_api/
├── app/
│   ├── api/
│   │   └── tron/
│   │       └── router.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── repositories.py
│   ├── schemas.py
│   └── settings.py
├── tests/
│   ├── conftest.py
│   ├── test_api_integration.py
│   └── test_database_unit.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Docker

### Сборка образа

```bash
docker build -t tronpy-api .
```

### Запуск в Docker

```bash
docker run -p 8000:8000 tronpy-api
```

## Лицензия

MIT 