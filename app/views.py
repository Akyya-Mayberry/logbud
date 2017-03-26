# python std libs
import logging

# 3rd party libs
from flask_login import LoginManager, login_required, login_user, logout_user
from flask import render_template, request, redirect, flash, url_for

# my libs
from app import app, db
from forms import LoggerLoginForm, VisitorSignInForm
from models import UserProfile, Visitor, Visit

# For flask_login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return UserProfile.query.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoggerLoginForm()
    if form.validate_on_submit():
        user = UserProfile.query.filter_by(email=form.email.data).first()

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
    form = VisitorSignInForm()

    # TODO:
        # implement
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname = form.firstname.data.lower()
            lastname = form.lastname.data.lower()
            visiting = form.visiting.data.lower()
            purpose = form.purpose.data.lower()

            # Check if visitor is new
            returning_visitor = Visitor.query.filter_by(firstname=firstname, lastname=lastname).first()
            if not returning_visitor:
                new_visitor = Visitor(firstname=firstname, lastname=lastname)
                db.session.add(new_visitor)
                db.session.commit()

                new_visitor = Visitor.query.filter_by(firstname=firstname, lastname=lastname).first()

                new_visit = Visit(visitor_id=new_visitor.id, visiting=visiting, purpose=purpose)
                db.session.add(new_visit)
                db.session.commit()

                return redirect('/log')

            # Returning visitor should not have active visit
            for visit in returning_visitor.visits:
                if visit.is_active():
                    flash('Visitor is already logged in!')
                    return redirect('/log/' + str(returning_visitor.id))

            # Log visitor
            new_visit = Visit(visitor_id=returning_visitor.id, visiting=visiting, purpose=purpose)
            db.session.add(new_visit)
            db.session.commit()
            return redirect('/log')

        flash("Form errors!")

    return render_template('logbud.html', form=form)


@app.route('/signout/<visitor_id>')
@login_required
def signout(visitor_id):
    """ Signs out a visitor """

    active_visits = Visit.query.filter_by(visitor_id=visitor_id, active=True)

    if active_visits:
        for visit in active_visits:
            visit.active = False
            db.session.commit()
        flash('Visitor successfully logged out.')
    else:
        flash('Visitor is currently not signed in.')

    return redirect('/log')


@app.route('/log')
@login_required
def log():
    """ Returns list of current visitors. """

    current_visitors = Visit.query.filter_by(active=True).all()

    return render_template('log.html', current_visitors=current_visitors)


@app.route('/log/<visitor_id>')
@login_required
def visitor(visitor_id):
    """ Returns details of a visitor. """

    visit = Visit.query.filter_by(visitor_id=visitor_id).first()
    return render_template('visitor.html', visit=visit)


@app.route('/log/activity')
@login_required
def activity():
    """ Returns all recorded log activity. """

    activity = Visit.query.all()

    return render_template('activity.html', activity=activity)
