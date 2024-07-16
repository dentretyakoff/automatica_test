# Automatica
API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.

### Функционал Recipes
Позволяет получить список Торговых точек привязанных к переданному номеру телефона и выполнить посещение в Торговую точку

### Технологии
 - Django==4.2
 - djangorestframework==3.15.2
 - PostgreSQL

### Установка и запуск проекта:
Клонируйте репозиторий и перейдите в него в командной строке:

```
git@github.com:dentretyakoff/automatica_test.git
```
```
cd automatica_test
```

Заполните .env по пример из .env.example

Установите виртуальное окружение:

```
python -m venv env
```
```
python3 -m venv env
```

Активируйте виртуальное окружение:

- На Windows: 
```
.\env\Scripts\activate
```
- На macOS и Linux: 
```
source env/bin/activate
```

Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустите PostgreSQL в докере:
```
docker-compose up -d
```

Выполните миграции:

```
python backend/manage.py migrate
```
```
python3 backend/manage.py migrate
```

Создайте суперпользователя: 

```
python backend/manage.py create_admin`
```
```
python3 backend/manage.py create_admin`
```

Запустите сервер:

```
python backend/manage.py runserver
```
```
python3 backend/manage.py runserver
```

### Доступ к API
API доступно по адресу http://localhost/api/v1/
GET - http://localhost/api/v1/points/ получить список точек пользователя
POST - http://localhost/api/v1/visit/ создать посещение точки

### Авторы
Денис Третьяков