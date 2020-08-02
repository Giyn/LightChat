from flask import render_template, flash, redirect, url_for, request, send_from_directory
from flask_login import login_user, login_required, current_user, logout_user
import os
from werkzeug.utils import secure_filename

from app import app, bcrypt, db
from app.forms import *
from app.email import send_reset_password_mail
from app.models import User, Post


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = PostTweetForm()
    if form.validate_on_submit():
        body = form.text.data
        post = Post(body=body)
        current_user.posts.append(post)
        db.session.commit()
        flash('You have post a new tweet', category='success')
    n_followers = len(current_user.followers)
    n_followed = len(current_user.followed)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, 5, False)
    return render_template('index.html', form=form, posts=posts,
                           n_followers=n_followers, n_followed=n_followed)


@app.route('/user_page/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    if user:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 3, False)
        return render_template('user_page.html', user=user, posts=posts)
    else:
        return '404'


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user:
        current_user.follow(user)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 3, False)
        return render_template('user_page.html', user=user, posts=posts)
    else:
        return '404'


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user:
        current_user.unfollow(user)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 3, False)
        return render_template('user_page.html', user=user, posts=posts)
    else:
        return '404'


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        if f.filename == '':
            flash('No selected file', category='danger')
            return render_template('edit_profile.html', form=form)
        if f and allowed_file(f.filename):
            real_filename = f.filename
            filename = secure_filename(f.filename)
            f.save(os.path.join('app', 'static', 'assets', real_filename))
            current_user.avatar_img = '/static/assets/' + real_filename
            db.session.commit()
            return redirect(url_for('user_page', username=current_user.username))
    return render_template('edit_profile.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! Registeration successfully!', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        # Check if password is matched
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # User exists and password matched
            login_user(user, remember=remember)
            flash('Login success', category='info')
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('User not exists or password not match', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/send_password_reset_request', methods=['GET', 'POST'])
def send_password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()
        send_reset_password_mail(user, token)
        flash('Password reset request mail is sent, please check your mailbox', category='info')
    return render_template('send_password_reset_request.html', form=form)


@app.route('/reset_password/<token>', methods=['GET','POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.check_reset_password_token(token)
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Your password reset is done, you can login with your new password now', category='info')
            return redirect(url_for('login'))
        else:
            flash('The user is not exist', category='info')
            return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join('static'), 'favicon.ico')