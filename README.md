# Flask Application with Application Factory Pattern

A modern Flask web application built using the application factory pattern, featuring user authentication, database integration, and a responsive Bootstrap UI.

## Features

- **Application Factory Pattern**: Modular and testable application structure
- **User Authentication**: Registration, login, and session management
- **Database Integration**: SQLAlchemy ORM with Flask-Migrate
- **Blueprint Architecture**: Organized routing with separate blueprints
- **Modern UI**: Bootstrap 5 with custom styling
- **Form Handling**: Flask-WTF with validation
- **Configuration Management**: Environment-based configuration

## Project Structure

```
app/
├── __init__.py          # Application factory
├── config.py            # Configuration classes
├── models.py            # Database models
├── auth/                # Authentication blueprint
│   ├── __init__.py
│   ├── routes.py
│   └── forms.py
├── main/                # Main application blueprint
│   ├── __init__.py
│   └── routes.py
├── static/              # Static files (CSS, JS, images)
│   └── css/
│       └── style.css
└── templates/           # Jinja2 templates
    ├── base.html
    ├── index.html
    ├── dashboard.html
    └── auth/
        ├── login.html
        └── register.html
```

## Installation

1. **Clone the repository** (or create the project structure as shown above)

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your configuration values.

5. **Initialize the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Usage

1. **Run the application**:
   ```bash
   python flask_app.py
   ```
   or
   ```bash
   flask run
   ```

2. **Access the application**:
   Open your browser and go to `http://localhost:5000`

3. **Register a new account** or **login** with existing credentials

## Configuration

The application supports multiple environments:

- **Development**: Debug mode enabled, SQLite database
- **Testing**: In-memory SQLite database for testing
- **Production**: Production-ready configuration

Set the `FLASK_CONFIG` environment variable to switch between configurations:
```bash
export FLASK_CONFIG=production
```

## Database Models

### User Model
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Hashed password
- `created_at`: Account creation timestamp
- `is_active`: Account status

## Blueprints

### Main Blueprint (`app/main/`)
- Home page (`/`)
- Dashboard (`/dashboard`) - requires authentication
- About page (`/about`)

### Auth Blueprint (`app/auth/`)
- Login (`/auth/login`)
- Register (`/auth/register`)
- Logout (`/auth/logout`)

## Development

### Adding New Features

1. **Create a new blueprint** for related functionality
2. **Define routes** in the blueprint's `routes.py`
3. **Create forms** in the blueprint's `forms.py` if needed
4. **Add templates** in the appropriate template directory
5. **Register the blueprint** in the application factory

### Database Changes

1. **Modify models** in `app/models.py`
2. **Generate migration**:
   ```bash
   flask db migrate -m "Description of changes"
   ```
3. **Apply migration**:
   ```bash
   flask db upgrade
   ```

### Running Tests

```bash
python -m pytest
```

## Deployment

1. **Set environment variables** for production
2. **Configure a production database** (PostgreSQL recommended)
3. **Set up a web server** (nginx + gunicorn recommended)
4. **Use environment-specific configuration**

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.
