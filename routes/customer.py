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
    b_datas = []
    if bs:
        fields = ('image', 'name', 'describe', )
        for b in bs:
            b_data = {}
            for k in fields:
                b_data[k] = b.__dict__.get(k)

            b_datas.append(b_data)

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
                    name=request.form.get('username'),
                ).save()
            except Exception as e:
                return jsonify(resp=0)

            return jsonify(resp=1)
        elif request.form.get('type') == 'yummy_business':
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
        if u.type == 'yummy_user':
            session['type'] = 'customer'
        else:
            session['type'] = 'restaurant'

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
    if not u:
        abort(400)

    userInfo = {}
    userInfo['email'] = u.username
    userInfo['phone'] = u.contact
    userInfo['name'] = u.name
    userInfo['address'] = '广东省广州市番禺区大学城中山大学至善园2号'
    userInfo['b_day'] = '1993-10-11'

    os =  Order.queryByCustomer(u.username)
    f_datas = []
    for o in os:
        f = {}
        f['id'] = o.id
        f['name'] = o.business
        f['date'] = o.createTime
        f['price'] = o.totalPrice
        f_datas.append(f)

    return render_template('myAccount.html', userInfo=userInfo, history=f_datas, order=f_datas)
