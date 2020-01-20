set FLASK_APP=setup.py 
flask db init
flask db migrate -m "optional message"
flask db upgrade