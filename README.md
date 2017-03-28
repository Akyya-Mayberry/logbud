# Logbud
Security log app that explores Flask and several flask extensions.

## Setup
1. Create a postgres database named *logbud*
2. Clone the logbud repository.
3. Create a virtual environment and activate it.
4. While inside your virtual environment, export the following two required environment variables
~~~.bash
export FLASK_APP=run.py
export DEBUG=1
~~~

  These variables informs Flask of the path to the logbud app and sets debugging to true.

5. Next we set up the database. While inside the root directory of the app where manage.py is located, excute the following,

~~~.bash
python manage.py db updgrade
~~~

6. Make sure you are inside the root directory of the application where *run.py* is located, and start the application.
~~~.bash
flask run
~~~

  This should start your server and direct you to http://localhost:5000 to view the application
  
## Testing out the application
1. To create a user that can log visitors, navigate to http://localhost:5000/admin and click on the *User Profile* tab.
  By clicking on the *Create* tab, you can create a new users.
  It is important that you DO NOT LEAVE THE PASSORD FIELD BLANK. Users must be assign a password, otherwise you will
  experience problems logging the user in.
2. Once the user is created, login the user at http://localhost:5000/login. 
3. The user can then begin to sign visitors in and out and view logs.
