from flask import Flask 

app = Flask (__name__)

@app.route('/')  # En flask-route, som tar besökare '/' till main sida samt gör om pyton kod till flask kod.

def home ():
    return "Hello World"

app. run()