# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template, request, session, abort, redirect, jsonify
from routes import app
from models import User, Business, Item, Order

@app.route('/')
@app.route('/home/')
def home():
    bs = Business.queryAll()
    fields = ('image', 'name', 'describe', )
    b_datas = []
    for b in bs:
        b_data = {}
        for k in fields:
            b_data[k] = b.__dict__.get(k)

        b_datas.append(b_data)
        b_data = {}

    return render_template('home.html',
        restaurants = b_datas)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        if request.form.get('type') == 'yummy_user':
            try:
                User(
                    username=request.form.get('username'),
                    contact=request.form.get('contact'),
                    hashpw=request.form.get('hashpw'),
                    name=request.form.get('name'),
                ).save()
            except Exception as e:
                print str(e)
                return jsonify(resp=0)

            return jsonify(resp=1)
        elif request.form.get('type') == 'yummy_business':
            print dict(request.form)
            try:
                Business(
                    username=request.form.get('username'),
                    contact=request.form.get('contact'),
                    hashpw=request.form.get('hashpw'),
                    name=request.form.get('name'),
                    address=request.form.get('address'),
                ).save()
            except Exception as e:
                return jsonify(resp=0)

            return jsonify(resp=1)
        else:
            return jsonify(resp=0)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    else:
        u = User.queryByUsername(request.form.get('username'))
        if not u:
            return jsonify(resp=0)

        if u.hashpw != request.form.get('hashpw'):
            return jsonify(resp=0)

        session['user'] = request.form.get('username')
        session['type'] = u.type
        return jsonify(resp=1)

@app.route('/logout/')
def logout():
    if not session.get('user', None):
        abort(400)

    session.pop('user')
    session.pop('type')
    return redirect('/')

@app.route('/myAccount/')
def myAccount():
    if not session.get('user', None):
        abort(400)

    u = User.queryByUsername(session['user'])

    userInfo = {}
    userInfo['email'] = '549425036@qq.com'
    userInfo['phone'] = '13826478796'
    userInfo['address'] = '广东省广州市番禺区大学城中山大学至善园2号'
    userInfo['b_day'] = '1993-10-11'
    userInfo['name'] = '黄佳博'
    history = []
    tmpHistory = {}
    tmpHistory['name'] = '四海一家'
    tmpHistory['date'] = '2014-5-6'
    tmpHistory['price'] = '258'
    for i in range(0,10):
      history.append(tmpHistory)
    
    for h in history:
      h['foods'] = []

    return render_template('myAccount.html', userInfo=userInfo, history=history, order=history, user=session)
