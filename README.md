# SichEnergo Website

Corporate website of **SichEnergo**, a manufacturer of power distribution equipment.

The website showcases the company's products and services, including:

* Power transformers
* Package transformer substations (KTP)
* Switchgear units (KSO)
* Engineering and electrical services
* Product galleries
* Technical drawings
* Specification questionnaires

---

## Technology Stack

* Python 3.11
* Django
* PostgreSQL
* HTML5
* CSS3
* Nginx
* Docker
* Amazon Web Services (AWS)
* Cloudinary
* CI/CD

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/sichenergo-site.git
cd sichenergo-site
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
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

### 5. Configure PostgreSQL

```sql
CREATE DATABASE sichenergo_db;

CREATE USER sichenergo_user
WITH PASSWORD 'your_password';

GRANT ALL PRIVILEGES
ON DATABASE sichenergo_db
TO sichenergo_user;
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 8. Collect Static Files

```bash
python manage.py collectstatic
```

### 9. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## Media Storage

All media files are uploaded through the Django administration panel and stored in **Cloudinary**, including:

* Product photographs
* Videos
* Technical drawings
* Specification questionnaires

Required environment variables:

```env
CLOUD_NAME
API_KEY
API_SECRET
```

---

## Logging

Application and Django events are logged to:

```text
django_debug.log
```

located in the project's root directory.

---

## Deployment

The project can be deployed to AWS using:

* Elastic Beanstalk
* EC2
* ECS

For production environments, it is recommended to use:

* Docker containers
* Nginx reverse proxy
* Automated CI/CD pipelines

---

## Project Structure

```text
sichenergo-site/
│
├── apps/
├── static/
├── templates/
├── media/
├── requirements.txt
├── manage.py
├── .env
└── README.md
```

---

## License

The source code is distributed under the MIT License.

Copyright © SichEnergo.

All photographs, videos, technical drawings, specification questionnaires, and other proprietary materials remain the intellectual property of SichEnergo and are protected by applicable copyright laws.

For details, see:

```text
LICENSE.md
```

---

## Contact Information

Website:
http://sich-energo.zp.ua/

Email:
[tovsichenergo@gmail.com](mailto:tovsichenergo@gmail.com)
