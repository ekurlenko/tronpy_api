## Установка и запуск

### 1. Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта:

```env
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=tronpy_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 2. Запуск 

Используйте Docker Compose для запуска приложения:

```bash
docker compose up --build
```
### 3. Тест
Перейдите по ссылке
```
http://0.0.0.0:8000/docs
```
