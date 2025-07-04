"""Main application entry point."""
import os
from flask_migrate import upgrade
from app import create_app, db
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    """Make database and models available in flask shell."""
    return {'db': db, 'User': User}


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # Create database tables
    upgrade()
    
    # Create or update user roles
    # Add any additional deployment tasks here


if __name__ == '__main__':
    app.run(debug=True)
