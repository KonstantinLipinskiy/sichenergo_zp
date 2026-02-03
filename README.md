# SichEnergo Website

Коммерческий сайт компании SichEnergo для представления продукции: трансформаторы, КТП, КСО, услуги, фото продукции, чертежи и опросные листы.

## Технологии
- Python 3.11 
- Django
- HTML
- CSS
- Amazon Web Services (AWS)
- CI/CD
- Cloudinary
- PostgreSQL

## Установка и запуск

### 1. Клонирование проекта
```
git clone https://github.com/your-repo/sichenergo-site.git
cd sichenergo-site
```
### 2. Создание и активация виртуального окружения
```
python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows
```
### 3. Установка зависимостей
```
pip install -r requirements.txt
```
### 4. Настройка переменных окружения
Создайте файл .env в корне проекта и укажите:
```
SECRET_KEY=your_secret_key
DEBUG=True

POSTGRES_DB=sichenergo_db
POSTGRES_USER=sichenergo_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

CLOUD_NAME=your_cloudinary_cloud_name
API_KEY=your_cloudinary_api_key
API_SECRET=your_cloudinary_api_secret
```
### 5. Настройка базы данных PostgreSQL
Настройка базы данных PostgreSQL
```
CREATE DATABASE sichenergo_db;
CREATE USER sichenergo_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE sichenergo_db TO sichenergo_user;
```
### 6. Применение миграций
```
python manage.py migrate
```
### 7. Создание суперпользователя
```
python manage.py createsuperuser
```
### 8. Сбор статики
```
python manage.py collectstatic
```
### 9. Запуск сервера разработки
```
python manage.py runserver
```
Сайт будет доступен по адресу: http://127.0.0.1:8000

## Хранение медиа
Все фото, видео, чертежи и опросные листы загружаются через админку и сохраняются в Cloudinary.

Для работы необходимо указать переменные окружения CLOUD_NAME, API_KEY, API_SECRET.

## Логирование
Все события Django и приложения entrance пишутся в файл django_debug.log в корне проекта.

## Деплой
Проект может быть развернут на AWS (Elastic Beanstalk / EC2 / ECS).

Рекомендуется использовать Docker и настроенный CI/CD pipeline для автоматического деплоя.

## Лицензия
Код распространяется по MIT License.

Фото, видео, чертежи и опросные листы защищены авторским правом © SichEnergo.

Подробнее см. файл LICENSE.md.

## Контакты
Веб‑сайт:  

Email: tovsichenergo@gmail.com