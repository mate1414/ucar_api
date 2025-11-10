# Incident API Service
API-сервис для учёта инцидентов.

## Быстрый запуск

1. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

Настройте базу данных:
```bash
alembic upgrade
```

```bash
uvicorn app.main:app --reload
```

Документация API: http://localhost:8000/docs

**Основные эндпоинты**

📝 Инциденты

Создать инцидент
```http
POST /incidents/
{
  "description": "Самокат не в сети",
  "source_id": 1
}
```

Получить список инцидентов
```http
GET /incidents/
GET /incidents/?status=new
GET /incidents/?skip=0&limit=10
```

Обновить статус инцидента
```http
PATCH /incidents/1
{
  "status": "in_progress"
}
```

Получить инцидент по ID
```http
GET /incidents/1
```

🔧 Источники

Создать источник
```http
POST /sources/
{
  "name": "Иванов Иван Иванович",
  "description": "Оператор сервиса Самокатов",
  "type": "operator",
}
```