# YaCut

## Описание
**YaCut** - cервис укорачивания ссылок, который заменяет длинную ссылку на короткую (до 16 символов).
Вариант сокращения может быть задан как самим пользователем, так и сгенерирован автоматически сервисом.
Все сокращения уникальны. Реализован Web-интерфейс для пользователей и REST API.

### Основные эндпоинты
/ - Web-интерфейс для генерации короткой ссылки

/<short_id>/ - Web-интерфейс для переадресации на исходную ссылку

/api/id/ - POST-запрос к API для генерации короткой ссылки

/api/id/<short_id>/ - GET-запрос для получения исходной ссылки из короткой


## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=white&color=000000)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=red&color=800000)](https://www.sqlalchemy.org/)

## Порядок действий для запуска проекта

***1. Клонировать репозиторий и перейти в папку c проектом***

```bash
git clone https://github.com/VitsVi/yacut.git
```

```bash
cd YaCut
```

***2. Cоздать и активировать виртуальное окружение***

*Для Windows*
```bash
python -m venv env
source venv/Scripts/Activate
```
*Для MacOS/Linux*
```shell
python3 -m venv env
source env/bin/activate
```

***3. Обновить менеджер pip и установить зависимости из файла requirements.txt***

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

***4. Применить миграции для создания базы данных***

```bash
flask db upgrade
```

***5. Создать файл .env и заполнить по примеру из файла env.example***

```bash
touch .env
```

***6. Запустить проект***
```bash
flask run
```

### Автор проекта

[VitsVi](https://github.com/VitsVi)
