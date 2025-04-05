# Coffee Orders API

Простой REST API-сервис для учёта заказов в кофейне

## Стек

- FastAPI
- SQLAlchemy + SQLite
- Alembic
- Pydantic
- Pytest

## Установка

```bash
git clone https://github.com/your-username/coffee-orders-api.git
cd coffee-orders-api
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
```

## Миграции (Alembic)

```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

## Запуск

```bash
uvicorn app.main:app --reload
```

Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Авторизация

Все запросы требуют заголовок:

```
X-API-Key: key
```

## Тесты

```bash
pytest
```
