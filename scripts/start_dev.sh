#!/bin/bash
#
# Prep environment to run flask cli and start server
# note: view->line endings in sublime to change line endings
echo "Prepping environment for Flask...."

activate () 
{
	echo "Activating virtual environment..."
	source env/Scripts/activate
	
	# turn on Flask debugging
	export FLASK_DEBUG=1
	
	# point Flask to the app to run
	export FLASK_APP=run.py
	
	echo "Starting the server...."
	flask run
}

activate

