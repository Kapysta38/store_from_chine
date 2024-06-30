# Store from Chine

Этот проект представляет собой систему для управления интернет-магазином, включающую API для работы с базой данных и бота для взаимодействия с пользователями. В проекте используется Python, FastAPI, SQLAlchemy и Alembic для миграций базы данных.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/store_from_Chine.git
    cd store_from_Chine
    ```

2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

3. Настройте переменные окружения:
    Создайте файл `.env` в корневой директории проекта и добавьте необходимые переменные окружения. Пример:
    ```env
    SECRET_KEY=your_secret_key
    POSTGRES_SERVER=localhost:port
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_DB=dbname
    ```

4. Выполните миграции базы данных:
    ```sh
    cd api_store
    alembic upgrade head
    cd ..
    ```

## Запуск

### API

1. Перейдите в директорию `api_store` и запустите FastAPI приложение:
    ```sh
    cd api_store
    uvicorn main:app --reload
    ```

### Бот

1. Перейдите в директорию `bot` и запустите бота:
    ```sh
    cd bot
    python run.py
    ```

## Структура каталогов

### Корневая директория

- `.env`: Файл с переменными окружения.
- `.gitignore`: Список файлов и директорий, игнорируемых Git.
- `LICENSE`: Лицензия проекта.
- `README.md`: Этот файл.
- `requirements.txt`: Список зависимостей проекта.

### `api_store/`

- `.env`: Переменные окружения для API.
- `alembic.ini`: Конфигурация Alembic для миграций базы данных.
- `main.py`: Главный файл для запуска FastAPI приложения.
- `__init__.py`: Инициализационный файл для пакета.

#### `alembic/`

- `env.py`: Основной файл настройки Alembic.
- `README`: Документация Alembic.
- `script.py.mako`: Шаблон для скриптов миграций.
- `versions/`: Папка с миграциями базы данных.

#### `app/`

- `api/`: Эндпоинты API и зависимости.
- `core/`: Конфигурации и безопасность.
- `crud/`: Операции CRUD (create, read, update, delete) для работы с базой данных.
- `db/`: Подключение к базе данных.
- `models/`: Модели базы данных (SQLAlchemy).
- `schemas/`: Схемы Pydantic.
- `shared/`: Общие типы данных.

### `bot/`

- `app.log`: Лог-файл приложения.
- `app.py`: Основной файл приложения бота.
- `run.py`: Скрипт для запуска бота.
- `api/`: Клиент для взаимодействия с API.
- `callbacks/`: Обработчики callback-ов.
- `config/`: Конфигурации логирования.
- `dependence/`: Обработка ошибок.
- `menu/`: Меню бота.
- `message_handlers/`: Обработчики сообщений.
- `settings/`: Настройки бота.
- `states/`: Состояния бота.
- `utils/`: Утилиты.

### `data/`

- `menu.json`: JSON файл с данными меню.

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле `LICENSE`.
