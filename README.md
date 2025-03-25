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

![](https://img.shields.io/badge/Python-3.9-black?style=flat&logo=python) 
![](https://img.shields.io/badge/Flask-2.0.2-black?style=flat&logo=flask)
![](https://img.shields.io/badge/SQLAlchemy-1.4.29-black?style=flat&logo=sqlalchemy)

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
