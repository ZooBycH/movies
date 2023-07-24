## Описание проекта
- Установка зависимостей
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Создание моделей (очистит БД и создаст все модели, указанные в импорте)
```shell
python create_tables.py
```

- Загрузка данных в базу
```shell
python load_fixture.py
```
Скрпит читает файл fixtures.json и загружает данные в базу. Если данные уже загружены - выводит соответсвующее сообщение. 

## Запуск проекта

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run
```

### CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run
```
## Запуск демонстрационного Frontend стенда
1. Скачать образ командой ```docker pull painassasin/node_cource_project:latest```
2. Запустить контейнер на 80 порту ```docker run -p 80:80 painassasin/node_cource_project```
- Образ сконфигурирован таким образом, что он будет ожидать backend на 5000 локальном порту
## Запуск тестов
```shell
pytest .
```

