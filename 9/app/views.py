from random import randint
from random import choice
from .forms import GetLucky 
from .forms import GetName

from app import app
from flask import render_template, request


def get_horoskop():
    a = ['In deinen Sternen steht, dass ', 'Auf dem Grunde der Kaffeetasse ist zu lesen, dass ', 'Das Orakel sagt, dass ']
    b = ['Du bald ', 'Du für immer und ewig ', 'Du in deinem Leben ']
    c = ['glücklich wirst.', 'Liebe findest.', 'reich und berühmt wirst.']
    horoskop = choice(a)+choice(b)+choice(c)
    return horoskop

def get_lucky_num(): 
	lucky_num = randint(1, 100)
	return lucky_num

@app.route('/', methods=['GET', 'POST'])
def get_name():
	form = GetName()
	if request.method == 'POST':
		name = form.name.data
		horoskop = get_horoskop()
		lucky_num = get_lucky_num()	
		return render_template('dein_hrsk.html', name=name.capitalize(), horoskop=horoskop, lucky_num=lucky_num)
	if request.method == 'GET':
		return render_template('hrsk.html', form=form)

@app.route('/name/', methods=['GET', 'POST'])
def name_length():
	form = GetName()
	if request.method == 'POST':
		name = form.name.data
		length = len(name)	
		return render_template('name.html', name=name.capitalize(), length=length)
	if request.method == 'GET':
		return render_template('hrsk.html', form=form)


    

