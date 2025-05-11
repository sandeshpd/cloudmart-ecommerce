# CloudMart

CloudMart is a feature-rich e-commerce platform built using Django, PostgreSQL, HTML, CSS, and JavaScript. It provides a seamless shopping experience for users and a robust management system for administrators.

## Features

### Implemented
- User authentication and authorization
- Product catalog with categories
- Responsive design for mobile and desktop
- Admin dashboard for managing products, orders, and users

### In Development
- Search functionality
- Shopping cart and checkout system
- Order management for users and admins

## Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Other Tools**: Bootstrap, jQuery

## Project Requirements

- Python 3.8+
- Django 5.0+
- PostgreSQL 12+
- Bootstrap 5 (optional but recommended)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sandeshpd/CloudMart.git
    cd CloudMart
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request or you can open issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [sandeshdha26@gmail.com](mailto:sandeshdha26@gmail.com).  