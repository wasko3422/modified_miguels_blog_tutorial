from flask import render_template, current_app
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=current_app.config['MAIL_USERNAME'],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))


def greeting_email(user, email):
    send_email('Welcome to Microblog',
               sender=current_app.config['MAIL_USERNAME'],
               recipients=[email],
               text_body=render_template('email/greetings.txt', user=user),
               html_body=render_template('email/greetings.html', user=user))