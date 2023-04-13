"""
materializadora 2022
BackEnd source
Holistic Diet application

"""
# APP Basic Settings
DEBUG = True
TESTING = False
ENV = "development"
SECURITY_PASSWORD_SALT = 'ultra-secreto'
CRET_KEY = ""

# DataBase Settings
BASE_DIR=os.path.dirname(os.path.realpath(__file__))


from flask import Flask

app=Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove
