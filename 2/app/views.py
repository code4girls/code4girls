from app import app
from flask import render_template
 
@app.route('/')
def lucky_static():
    return render_template('html.html')
