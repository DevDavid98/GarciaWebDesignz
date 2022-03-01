# import all modules for website to run
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, render_template, request, url_for, flash
from flask_mail import Mail, Message
from sqlalchemy.exc import IntegrityError
import os

# The environmental variables for email and password for google
EMAIL_USERNAME = os.getenv('My_Email')
EMAIL_PASSWORD = os.getenv('THE_PASSWORD')

# Initiate Flask app
app = Flask(__name__)

# All email configs for flask_mail
app.config['DEBUG'] = True
# app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Port 25 if ssl and tls is all wrong
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = EMAIL_USERNAME
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = ('Garcia Web Designz', EMAIL_USERNAME)
app.config['MAIL_MAX_EMAILS'] = 1
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

# Create database integrity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Client.db'
db = SQLAlchemy(app)


# Created database of clients
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Client Name', db.String())
    email = db.Column('Client Email', db.String(), unique=True)
    number = db.Column('Client Number', db.String())
    message = db.Column('Client Message', db.Text())


# Home page
# If any one sees this backend code yes I know the code is WET as hell..
# Ill make it dry later in the future.... ;)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = ('\
                \nClient name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('index'))

    return render_template('index.html')


# about me page
@app.route('/me', methods=['GET', 'POST'])
def me():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = (
                'Client name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('me'))

    return render_template('me.html')


# About company page
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = (
                'Client name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('about'))

    return render_template('about.html')


# my work page
@app.route('/work', methods=['GET', 'POST'])
def my_work():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = (
                'Client name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('my_work'))

    return render_template('my_work.html')


# Education page
@app.route('/education', methods=['GET', 'POST'])
def education():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = (
                'Client name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('education'))

    return render_template('education.html')


@app.route('/information', methods=['GET', 'POST'])
def information():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = (
                'Client name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('information'))

    return render_template('information.html')


@app.route('/pricing', methods=['GET', 'POST'])
def pricing():
    if request.method == "POST":
        try:
            new_client = Client(
                name=request.form['name'],
                email=request.form['email'],
                number=request.form['number'],
                message=request.form['message'])

            db.session.add(new_client)
            db.session.commit()

            msg = Message('Welcome to Garcia Web Designz!',
                          recipients=[new_client.email])

            msg.html = render_template('email_template.html')
            mail.send(msg)
            my_msg = Message('New form submission.',
                             recipients=[EMAIL_USERNAME])

            my_msg.body = (
                'Client name: {} \n \
                Client email: {} \n \
                Client number: {} \n \
                Client message: {}'.format(new_client.name,
                                           new_client.email,
                                           new_client.number,
                                           new_client.message))

            mail.send(my_msg)

        except IntegrityError:
            db.session.rollback()

        redirect(url_for('pricing'))

    return render_template('pricing.html')


# 404 page
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
