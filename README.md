This project is a Django-based web application designed to manage listings, users, categories, and locations.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Valijonzoda/somonTJ.git
    cd somonTJ
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your configuration variables:
    ```plaintext
    MYSQL_DEFAULT_DATABASE=your_database_name
    MYSQL_USER=your_database_user
    MYSQL_PASSWORD=your_database_password
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    ```

5. Apply the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Configuration

Make sure to configure your database and other settings in the `.env` file. The project uses `python-dotenv` to manage environment variables.
