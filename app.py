# Python libs

# 3rd party libs
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

# My libs
import models


app = Flask(__name__, static_url_path="/static")
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'oribooboo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///logbud'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return models.UserProfile.query.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = models.LoggerLoginForm()
    if form.validate_on_submit():
        user = models.UserProfile.query.filter_by(email=form.email.data).first()

        # Login and validate the user.
        if user:
            if user.password == form.password.data:
                user.authenticated = True
                user.active = True
                login_user(user, remember=True)

                # flash('Logged in successfully.')

                next = request.args.get('next')
                # TODO:
                # is_safe_url should check if the url is safe for redirects.
                # See http://flask.pocoo.org/snippets/62/ for an example.
                # if not flask_login.is_safe_url(next):
                #     return app.abort(400)
                return redirect(next or url_for('.logbud'))

        # TODO:
            # Set up registering new users

        flash("Invalid credentials!")
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    # flash('Logged out successfully.')
    return redirect('/')


@app.route('/logbud', methods=['GET', 'POST'])
@login_required
def logbud():
    form = models.VisitorSignInForm()

    # TODO:
        # implement
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            visiting = form.visiting.data
            purpose = form.purpose.data

            # Log visitor
            new_visitor = models.Visitor(firstname=firstname, lastname=lastname, visiting=visiting, purpose=purpose)
            models.db.session.add(new_visitor)
            models.db.session.commit()

            return redirect('/log')

        flash("Form errors!")

    return render_template('logbud.html', form=form)


@app.route('/log')
@login_required
def log():

    return render_template('log.html')


if __name__ == "__main__":
    models.connect_to_db(app)
    app.run()
