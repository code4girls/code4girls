from random import randint
from random import choice
from .forms import GetLucky 
from .forms import GetName

from app import app
from flask import render_template
 
@app.route('/')
def lucky_static():
    lucky_num = randint(1, 100)
    return render_template('simple.html', lucky_num=lucky_num)
    
#@app.route('/<max>/')
#def lucky_max(max):
 #   lucky_num = randint(1, int(max))
  #  return render_template('simple.html', lucky_num=lucky_num)


@app.route('/horoskop/')
def get_horoskop():
    a = ['In deinen Sternen steht, dass ', 'Auf dem Grunde der Kaffeetasse ist zu lesen, dass ', 'Das Orakel sagt, dass ']
    b = ['Du bald ', 'Du für immer und ewig ', 'Du in deinem Leben ']
    c = ['glücklich wirst.', 'Liebe findest.', 'reich und berühmt wirst.']
    horoskop = choice(a)+choice(b)+choice(c)
    lucky_num = randint(1, 100)
    return render_template('horoskop.html', horoskop=horoskop, lucky_num=lucky_num)

@app.route('/game/')
def game():
    game_nums = []
    while len(game_nums) < 5:
        n = randint(1, 10)
        if not n in game_nums:
            game_nums.append(n)
    return render_template('game.html', game_nums = game_nums)

@app.route('/nums/', methods=['GET', 'POST'])
def get_nums():
	form = GetLucky()
	return render_template('get_lucky.html', form=form)

@app.route('/hrsk/', methods=['GET', 'POST'])
def get_name():
	form = GetName()
	return render_template('hrsk.html', form=form)

#@app.route('/<name>/')
#def name_length(name):
#    length = len(name)
#    return render_template('name.html', name=name.capitalize(), length=length)

