# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import datetime
from flask import render_template, request, session, abort, redirect, jsonify, Response
from routes import app
from models import Business, User, Item, Order

@app.route('/myRestaurant/')
def showMyRestaurant():
    if not session.get('user', None):
        abort(400)

    b = Business.queryByUsername(session['user'])
    if not b:
        abort(400)

    info = {}
    fields = ('image', 'name', 'address', 'contact', 'describe')
    for f in fields:
        info[f] = getattr(b, f)

    orders = Order.queryByBusiness(session['user'])
    forders = []
    for o in orders:
        forders.append({
            'orderId': o.id,
            'date': o.createTime,
            'price': o.totalPrice
        })
    foods = Item.queryBySupplier(session['user'])
    if foods:
        categorys = '，'.join([x.category for x in foods])
        info['mainFoods'] = categorys

    return render_template('myRestaurant.html', info=info, foods=foods, order=forders)

@app.route('/restaurantDetail/', methods=['GET', 'POST'])
def showRestaurantDetail():
    if request.method == 'GET':
        info = Business.queryByName(request.args.get('name', None))
        if not info:
            abort(404)

        foods = Item.queryBySupplier(info.username)
        return render_template('restaurantDetail.html', info=info, foods=foods)

@app.route('/listDisplay/')
def listDisplay():
    bs = Item.queryBusinessByItemCategory(request.args.get('', None))
    b_datas = [Business.queryByUsername(x) for x in bs]

    return render_template('listDisplay.html', restaurants=b_datas)

@app.route('/order/', methods=['GET', 'POST'])
def getOrderInfo():
    if request.method == 'POST':
        o = Order.queryById(request.form.get('orderId', None))
        f_data = {}
        if not o:
            return Response(json.dumps(f_data), mimetype='application/json')

        f_data['orderId'] = str(o.id)
        f_data['restaurant'] = o.business
        f_data['date'] = o.createTime.strftime('%Y-%m-%d %H:%M:%S')
        f_data['customer'] = o.customer
        f_data['totalPrice'] = o.totalPrice
        b = Business.queryByUsername(o.business)
        f_data['address'] = b.address
        f_data['contact'] = b.contact
        detail = []
        foods = o.items.split(',')
        counts = o.items.split(',')
        prices = o.items.split(',')
        for x, y, z in zip(foods, counts, prices):
            detail.append({
                'name': x,
                'count': y,
                'price': z
            })

        f_data['detail'] = detail
        return Response(json.dumps(f_data), mimetype='application/json')

@app.route('/order/create/', methods=['GET', 'POST'])
def createOrder():
    if request.method == 'POST':
        foods = request.form.get('foods', None)
        counts = request.form.get('counts', None)
        prices = request.form.get('prices', None)

        if not foods:
            return jsonify(resp=0)

        if foods.count(',') != counts.count(',') != prices.count(','):
            return jsonify(resp=0)

        restaurant = Business.queryByName(request.form.get('restaurant')).username
        pricesArr = prices.split(',')
        totalPrice = reduce(lambda l, r: int(l) + int(r), pricesArr, 0)
        try:
            Order(
                items=foods,
                counts=counts,
                prices=prices,
                customer=session['user'],
                business=restaurant,
                totalPrice=totalPrice).save()
        except Exception, e:
            print str(e)
            return jsonify(resp=0)
        else:
            return jsonify(resp=1)

@app.route('/food/remove/', methods=['GET', 'POST'])
def removeItem():
    if request.method == 'POST':
        name = request.form.get('name', None)
        resp = int(Item.deleteByName(name))
        return jsonify(resp=resp)

@app.route('/food/create/', methods=['GET', 'POST'])
def createItem():
    if request.method == 'POST':
        fields = ('name', 'price', 'category', 'describe')
        fdata = {}
        for f in fields:
            fdata[f] = request.form.get(f)

        fdata['supplier'] = session['user']
        print fdata
        try:
            Item(**fdata).save()
        except Exception, e:
            print str(e)
            return jsonify(resp=0)
        else:
            return jsonify(resp=1)
