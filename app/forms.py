from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField() # 机器人验证
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already token, please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already token, please choose another one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Email not exists.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


class PostTweetForm(FlaskForm):
    text = TextAreaField('Say something ...', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Post Text')


class UploadPhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')