"""Main application routes."""
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    """Home page."""
    return render_template('index.html', title='Home')
