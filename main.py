import json
from random import choice
import secrets

from flask import Flask, render_template, request
import os
# CW - classwork
# HW - homework
# AW - additional work
from login_form import EmergencyAccess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfghvH$(()#(R@HFEFWA'
PROFESSIONS = ['Врач', 'Инженер', 'Строитель', 'Программист', 'Анимешник']
FORM_AUTO_ANSWER = {
    'title': 'JoJo in Mars',
    'surname': 'Joseph',
    'name': 'Joestar',
    'education': 'Среднее общее',
    'profession': 'Защитник планеты земля',
    'sex': 'male',
    'motivation': 'Раньше Дио добраться до Марса',
    'ready': 'Да'
}
CREW = ['Kujo Jotaro', 'Joseph Joestar', 'Giorno Giovanna', 'Dio Brando']
DIRNAME = 'static/img/carousel_img/'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Начало')


# beginning CW (1)
@app.route('/<title>')
def title(name):
    return render_template('index.html', title=name)
# ending of CW (1)


# beginning CW (2)
@app.route('/training/<prof>')
def training(prof):
    return render_template('profession.html', prof=prof)
# ending of CW (2)


# beginning CW (3)
@app.route('/list_prof/<type>')
def prof_list(type):
    return render_template('profession_list.html', professions=PROFESSIONS, type=type)
# ending of CW (3)


# beginning CW (4)
@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', **FORM_AUTO_ANSWER)
# ending of CW (4)


# beginning CW (5)
@app.route('/login')
def login():
    form = EmergencyAccess()
    return render_template('login.html', form=form)
# ending of CW (5)


# beginning HW (1)
@app.route('/distribution')
def distribution():
    return render_template('rooms.html', people=CREW)
# ending of HW (1)


# beginning HW (2)
@app.route('/table/<sex>/<age>')
def rooms_decoration(sex, age):
    return render_template('table.html', sex=sex, age=int(age))
# ending of HW (2)


# beginning AW (1)
@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'GET':
        imgs = os.listdir(DIRNAME)
        print(imgs)
        return render_template('gallery.html', images=imgs)
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/carousel_img/' + f.filename, 'wb') as ass:
            ass.write(f.read())
        return 'Перезагрузи страницу(Нажми на адресную строку и Enter)'
# ending of AW (1)


# beginning AW (2)
@app.route('/member', methods=['POST', 'GET'])
def member():
    with open('crew.json', 'r') as ass:
        data = json.load(ass)
    data = secrets.choice(data)
    img = data['image']
    fullname = data['name'] + ' ' + data['surname']
    return render_template('member.html', image=img, fullname=fullname, description=data['profession'])
# ending of AW (2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
