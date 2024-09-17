# Create authetnication blueprints
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.forms import LoginForm
from app import db

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.dashboard'))
  
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('auth.login'))
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('main.dashboard'))
  else:
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))